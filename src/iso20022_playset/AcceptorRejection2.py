import base_types
import Max500Text
import Max100KBinary
import RejectReason1Code

class AcceptorRejection2(base_types._BaseFieldType):

	__slots__ = ["_MsgInErr", "_AddtlInf", "_RjctRsn"]
	@property
	def MsgInErr(self):
		return self._MsgInErr

	@MsgInErr.setter
	def MsgInErr(self, value):
		self._MsgInErr = value if type(value) != auto else self.make_default("MsgInErr")

	@MsgInErr.deleter
	def MsgInErr(self):
		del self._MsgInErr
		self._MsgInErr = None

	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def RjctRsn(self):
		return self._RjctRsn

	@RjctRsn.setter
	def RjctRsn(self, value):
		self._RjctRsn = value if type(value) != auto else self.make_default("RjctRsn")

	@RjctRsn.deleter
	def RjctRsn(self):
		del self._RjctRsn
		self._RjctRsn = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='MsgInErr', type=Max100KBinary, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AddtlInf', type=Max500Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RjctRsn', type=RejectReason1Code, min=1, max=1, mutex_group=None, array=False),
	))

