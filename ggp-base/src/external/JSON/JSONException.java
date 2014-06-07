package external.JSON

/**
 * The JSONException is thrown by the JSON.org classes when things are amiss.
 * @author JSON.org
 * @version 2010-12-24
 */
class JSONException(Exception):
    serialVersionUID = 0  # int 
    cause = Throwable()

    /**
     * Constructs a JSONException with an explanatory message.
     * @param message Detail about the reason for the exception.
     */
    def JSONException(String message):
        super(message)

    def JSONException(Throwable cause):
        super(cause.getMessage())
        self.cause = cause

    def getCause():  # Throwable
        return self.cause
