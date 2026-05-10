from . import base_types
from .Max35Text import Max35Text
from .GenericIdentification30 import GenericIdentification30
from .QueryReference2 import QueryReference2
from .Max5NumericText import Max5NumericText
from .Frequency25Choice import Frequency25Choice
from .StatementUpdateTypeCodeAndDSSCode1Choice import StatementUpdateTypeCodeAndDSSCode1Choice
from .DateAndDateTime1Choice import DateAndDateTime1Choice

class Report6(base_types._BaseFieldType):

	__slots__ = ["_RptDtTm", "_RptId", "_NtceTp", "_QryRef", "_UpdTp", "_RptNb", "_Frqcy"]
	@property
	def RptDtTm(self):
		return self._RptDtTm

	@RptDtTm.setter
	def RptDtTm(self, value):
		self._RptDtTm = value if type(value) != base_types.auto else self.make_default("RptDtTm")

	@RptDtTm.deleter
	def RptDtTm(self):
		del self._RptDtTm
		self._RptDtTm = None

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if type(value) != base_types.auto else self.make_default("RptId")

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = None

	@property
	def NtceTp(self):
		return self._NtceTp

	@NtceTp.setter
	def NtceTp(self, value):
		self._NtceTp = value if type(value) != base_types.auto else self.make_default("NtceTp")

	@NtceTp.deleter
	def NtceTp(self):
		del self._NtceTp
		self._NtceTp = None

	@property
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if type(value) != base_types.auto else self.make_default("QryRef")

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = None

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if type(value) != base_types.auto else self.make_default("UpdTp")

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = None

	@property
	def RptNb(self):
		return self._RptNb

	@RptNb.setter
	def RptNb(self, value):
		self._RptNb = value if type(value) != base_types.auto else self.make_default("RptNb")

	@RptNb.deleter
	def RptNb(self):
		del self._RptNb
		self._RptNb = None

	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if type(value) != base_types.auto else self.make_default("Frqcy")

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RptDtTm', type=DateAndDateTime1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtceTp', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=QueryReference2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=StatementUpdateTypeCodeAndDSSCode1Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Frqcy', type=Frequency25Choice, min=0, max=1, mutex_group=None, array=False),
	))

