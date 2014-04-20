package external.JSON;

/**
 * The JSONException is thrown by the JSON.org classes when things are amiss.
 * @author JSON.org
 * @version 2010-12-24
 */
class JSONException(Exception):
    private static final long serialVersionUID = 0;
    private Throwable cause;

    /**
     * Constructs a JSONException with an explanatory message.
     * @param message Detail about the reason for the exception.
     */
    public JSONException(String message):
        super(message);
    }

    public JSONException(Throwable cause):
        super(cause.getMessage());
        this.cause = cause;
    }

    def getCause():  # Throwable
        return this.cause;
    }
