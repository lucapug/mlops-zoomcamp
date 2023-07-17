## Module 6 - Best practices

### Unit tests with Pytest

To ease a constant control on the code created over time, one of the suggested best practices consists in the definition of additional code to test single logic operations (unit tests).

The first step for doing unit tests is refactoring our code. This involves decomposing functions that do many things in multiple simple modules, each one responsible of a single logic operation. In the refactored version of the code possibly all the global variables should disappear. 

Once refactored our target code (in our case `batch.py` which reads a batch file and produce a file of inferences), the next step is organizing tests in a second script `test_batch.py`. This module is created in a `tests` folder and the folder hosts a package (with \_\_init\_\_.py) . The adoption of a dunder (double underscore) file ease to define a package and specify its boundaries and to manage the import of modules from the package

ususally each unit test is a single method that takes care of a corresponding function in the refactored version of the target code. Its typical form is to build a simplified version of the piece of logic to be tested (eventually making use of mocks to mimic some complex components). This simplified version applied to basic inputs gives an **expected result** to be compared with tha **actual result** form the target function. The comparison is done through an **assertion** at the end of the test function. 

Then pytest must be installed (as dev dependency) in the virtual environment.

I am using VSCode IDE, in which tha Python extension allows to configure pytest from the Testing button on the left side. **Pay attention** that to successfully recognize the tests folder The root folder (the one opened in VSC at the beginning of the coding session) must be the parent folder (in my case `my_hw`)

### Integration tests with docker-compose

generally a python module of a minimum complexity is sructured in functions and methods that interact each other to accomplish the final task. Integration tests (as opposed to unit tests) are meant to verify the correct functioning of these interactions. 
In the lectures (where the use case is a stream deployment) there are two integration tests, one to check the correct functioning of the lambda function after the dockerization (test\_docker); the second ont to check the right functioning of the output prediction stream (test\_kinesis). The stream service is a local emulation of an aws kinesis stream service, obtained through localstack library (we adopt the version installed as a docker service as coded in the `docker-compose.yaml` file
In my\_hw there is a single integration test which verify the correct storage in a AWS S3 bucket (again simulated as a docker-compose service, through localstack)

