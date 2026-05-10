from . import base_types
from .StatusReasonInformation10 import StatusReasonInformation10
from .Status6Code import Status6Code
from .SecuritiesAccount19 import SecuritiesAccount19

class SecuritiesAccountStatus2(base_types._BaseFieldType):

	__slots__ = ["_StsRsn", "_RltdSctiesAcct", "_Sts"]
	@property
	def StsRsn(self):
		return self._StsRsn

	@StsRsn.setter
	def StsRsn(self, value):
		self._StsRsn = value if type(value) != base_types.auto else self.make_default("StsRsn")

	@StsRsn.deleter
	def StsRsn(self):
		del self._StsRsn
		self._StsRsn = None

	@property
	def RltdSctiesAcct(self):
		return self._RltdSctiesAcct

	@RltdSctiesAcct.setter
	def RltdSctiesAcct(self, value):
		self._RltdSctiesAcct = value if type(value) != base_types.auto else self.make_default("RltdSctiesAcct")

	@RltdSctiesAcct.deleter
	def RltdSctiesAcct(self):
		del self._RltdSctiesAcct
		self._RltdSctiesAcct = None

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='StsRsn', type=StatusReasonInformation10, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='RltdSctiesAcct', type=SecuritiesAccount19, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=Status6Code, min=1, max=1, mutex_group=None, array=False),
	))

