package it.smartcommunitylabdhub.runtime.hpcdl.framework.config;

import it.smartcommunitylabdhub.commons.services.RunnableStore;
import it.smartcommunitylabdhub.runtime.hpcdl.framework.infrastructure.HPCDLFramework;
import it.smartcommunitylabdhub.runtime.hpcdl.framework.runnables.HPCDLRunnable;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class HPCDLFrameworkConfig {

    @Bean
    public RunnableStore<HPCDLRunnable> hpcdlRunnableStoreService(
        RunnableStore.StoreSupplier storeSupplier
    ) {
        return storeSupplier.get(HPCDLRunnable.class);
    }

    
    @Bean
    public HPCDLFramework hpcdlFramework() {
        return new HPCDLFramework();
    }

}
