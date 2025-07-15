package it.smartcommunitylabdhub.runtime.hpcdl.framework.listeners;

import it.smartcommunitylabdhub.commons.exceptions.StoreException;
import it.smartcommunitylabdhub.commons.models.enums.State;
import it.smartcommunitylabdhub.commons.services.RunnableStore;
import it.smartcommunitylabdhub.runtime.hpcdl.framework.exceptions.HPCDLFrameworkException;
import it.smartcommunitylabdhub.runtime.hpcdl.framework.infrastructure.HPCDLFramework;
import it.smartcommunitylabdhub.runtime.hpcdl.framework.runnables.HPCDLRunnable;
import it.smartcommunitylabdhub.runtimes.events.RunnableChangedEvent;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.ApplicationEventPublisher;
import org.springframework.context.event.EventListener;
import org.springframework.scheduling.annotation.Async;
import org.springframework.stereotype.Component;
import org.springframework.util.Assert;

@Component
@Slf4j
public class HPCDLRunnableListener {

    @Autowired
    HPCDLFramework framework;

    @Autowired
    ApplicationEventPublisher eventPublisher;

    @Autowired
    private RunnableStore<HPCDLRunnable> runnableStore;

    @Async
    @EventListener
    public void listen(HPCDLRunnable runnable) {
        Assert.notNull(runnable, "runnable can not be null");
        Assert.hasText(runnable.getId(), "runnable id can not be null or empty");
        log.info("Receive runnable for execution: {}", runnable.getId());

        String state = runnable.getState();

        try {
            runnable =
                switch (State.valueOf(state)) {
                    case State.READY -> {
                        yield framework.run(runnable);
                    }
                    case State.STOP -> {
                        yield framework.stop(runnable);
                    }
                    case State.DELETING -> {
                        yield framework.delete(runnable);
                    }
                    default -> {
                        yield null;
                    }
                };

            if (runnable != null) {
                try {
                    // If runnable is deleted, remove from store
                    if (runnable.getState().equals(State.DELETED.name())) {
                        runnableStore.remove(runnable.getId());
                    } else {
                        runnableStore.store(runnable.getId(), runnable);
                    }
                } catch (StoreException e) {
                    log.error("Error with store: {}", e.getMessage());
                }
            }
        } catch (HPCDLFrameworkException e) {
            // Set runnable to error state send event
            log.error("Error with k8s: {}", e.getMessage());
            runnable.setState(State.ERROR.name());
            runnable.setError(e.toError());

            try {
                runnableStore.store(runnable.getId(), runnable);
            } catch (StoreException ex) {
                log.error("Error with store: {}", ex.getMessage());
            }
        } finally {
            if (runnable != null) {
                log.debug("Processed runnable {}", runnable.getId());

                // Publish event to Run Manager
                eventPublisher.publishEvent(RunnableChangedEvent.build(runnable, state));
            }
        }
    }
}
