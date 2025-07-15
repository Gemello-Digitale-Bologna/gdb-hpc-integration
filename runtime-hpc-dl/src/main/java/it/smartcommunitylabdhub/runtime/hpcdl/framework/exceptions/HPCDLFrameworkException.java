package it.smartcommunitylabdhub.runtime.hpcdl.framework.exceptions;

import it.smartcommunitylabdhub.commons.exceptions.FrameworkException;

public class HPCDLFrameworkException  extends FrameworkException  {

    public HPCDLFrameworkException(String message) {
        super(message);
    }

    public HPCDLFrameworkException(String message, Throwable cause) {
        super(message, cause);
    }

    public String toError() {
        StringBuilder sb = new StringBuilder("hpcdl: ");
        if (getMessage() != null) {
            sb.append(getMessage());
        }
        return sb.toString();
    }
}
