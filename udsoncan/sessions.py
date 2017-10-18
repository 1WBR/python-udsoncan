import inspect
import sys

def from_id(given_id):
	return Session.from_id(given_id)

class Session:
	_sessionid = None

	@classmethod	
	def get_id(cls):
		return cls._sessionid

	@classmethod
	def from_id(cls, given_id):
		for name, obj in inspect.getmembers(sys.modules[__name__]):
			if hasattr(obj, "__bases__") and cls in obj.__bases__:
				if obj.get_id() == given_id:
					return obj

class DefaultSession(Session):
	_sessionid = 0x01

class ProgrammingSession(Session):
	_sessionid = 0x02

class ExtendedDiagnosticSession(Session):
	_sessionid = 0x03

class SafetySystemDiagnosticSession(Session):
	_sessionid = 0x04