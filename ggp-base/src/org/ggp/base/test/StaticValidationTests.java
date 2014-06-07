package org.ggp.base.test

import org.ggp.base.util.game.TestGameRepository
import org.ggp.base.validator.StaticValidator
import org.ggp.base.validator.ValidatorException
import org.junit.Test

class StaticValidationTests(object):

    @Test
    def void testConn4Validation() throws Exception 
        validate("connectFour")

    @Test
    def void testSimpleMutexValidation() throws Exception 
        validate("simpleMutex")

    @Test(expected=ValidatorException.class)
    def void test1AValidation() throws Exception 
        validate("test_case_1a")

    @Test
    def void test1BValidation() throws Exception 
        validate("test_case_1b")

    @Test
    def void test2AValidation() throws Exception 
        validate("test_case_2a")

    @Test
    def void test2BValidation() throws Exception 
        validate("test_case_2b")

    @Test
    def void test2CValidation() throws Exception 
        validate("test_case_2c")

    @Test(expected=ValidatorException.class)
    def void test3AValidation() throws Exception 
        validate("test_case_3a")

    @Test(expected=ValidatorException.class)
    def void test3BValidation() throws Exception 
        validate("test_case_3b")

    @Test
    def void test3CValidation() throws Exception 
        validate("test_case_3c")

    @Test
    def void test3DValidation() throws Exception 
        validate("test_case_3d")

    @Test(expected=ValidatorException.class)
    def void test3EValidation() throws Exception 
        validate("test_case_3e")

    @Test(expected=ValidatorException.class)
    def void test3FValidation() throws Exception 
            validate("test_case_3f")

    @Test
    def void test4AValidation() throws Exception 
        validate("test_case_4a")

    @Test
    def void test5AValidation() throws Exception 
        validate("test_case_5a")

    @Test
    def void test5BValidation() throws Exception 
        validate("test_case_5b")

    @Test
    def void test5CValidation() throws Exception 
        validate("test_case_5c")

    @Test(expected=ValidatorException.class)
    def void testCleanNotDistinctValidation() throws Exception 
        validate("test_clean_not_distinct")

    @Test(expected=ValidatorException.class)
    def void testFunctionAritiesDiffer() throws Exception 
    	validate("test_invalid_function_arities_differ")

    @Test(expected=ValidatorException.class)
    def void testSentenceAritiesDiffer() throws Exception 
    	validate("test_invalid_sentence_arities_differ")

    @Test
    def void testTicTacToeValidation() throws Exception 
        validate("ticTacToe")

    protected void validate(String gameName) throws Exception 
        new StaticValidator().checkValidity(new TestGameRepository().getGame(gameName))
