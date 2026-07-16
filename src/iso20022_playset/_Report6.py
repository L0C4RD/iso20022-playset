# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime1Choice
from . import Frequency25Choice
from . import GenericIdentification30
from . import Max35Text
from . import Max5NumericText
from . import QueryReference2
from . import StatementUpdateTypeCodeAndDSSCode1Choice

class Report6(base_types._BaseFieldType):

	__slots__ = ["_Frqcy", "_NtceTp", "_QryRef", "_RptDtTm", "_RptId", "_RptNb", "_UpdTp"]
	@property
	def Frqcy(self):
		return self._Frqcy

	@Frqcy.setter
	def Frqcy(self, value):
		self._Frqcy = value if value is not None else base_types.UninitialisedField(self, 'Frqcy', Frequency25Choice, False)

	@Frqcy.deleter
	def Frqcy(self):
		del self._Frqcy
		self._Frqcy = base_types.UninitialisedField(self, 'Frqcy', Frequency25Choice, False)

	@property
	def NtceTp(self):
		return self._NtceTp

	@NtceTp.setter
	def NtceTp(self, value):
		self._NtceTp = value if value is not None else base_types.UninitialisedField(self, 'NtceTp', GenericIdentification30, False)

	@NtceTp.deleter
	def NtceTp(self):
		del self._NtceTp
		self._NtceTp = base_types.UninitialisedField(self, 'NtceTp', GenericIdentification30, False)

	@property
	def QryRef(self):
		return self._QryRef

	@QryRef.setter
	def QryRef(self, value):
		self._QryRef = value if value is not None else base_types.UninitialisedField(self, 'QryRef', QueryReference2, False)

	@QryRef.deleter
	def QryRef(self):
		del self._QryRef
		self._QryRef = base_types.UninitialisedField(self, 'QryRef', QueryReference2, False)

	@property
	def RptDtTm(self):
		return self._RptDtTm

	@RptDtTm.setter
	def RptDtTm(self, value):
		self._RptDtTm = value if value is not None else base_types.UninitialisedField(self, 'RptDtTm', DateAndDateTime1Choice, False)

	@RptDtTm.deleter
	def RptDtTm(self):
		del self._RptDtTm
		self._RptDtTm = base_types.UninitialisedField(self, 'RptDtTm', DateAndDateTime1Choice, False)

	@property
	def RptId(self):
		return self._RptId

	@RptId.setter
	def RptId(self, value):
		self._RptId = value if value is not None else base_types.UninitialisedField(self, 'RptId', Max35Text, False)

	@RptId.deleter
	def RptId(self):
		del self._RptId
		self._RptId = base_types.UninitialisedField(self, 'RptId', Max35Text, False)

	@property
	def RptNb(self):
		return self._RptNb

	@RptNb.setter
	def RptNb(self, value):
		self._RptNb = value if value is not None else base_types.UninitialisedField(self, 'RptNb', Max5NumericText, False)

	@RptNb.deleter
	def RptNb(self):
		del self._RptNb
		self._RptNb = base_types.UninitialisedField(self, 'RptNb', Max5NumericText, False)

	@property
	def UpdTp(self):
		return self._UpdTp

	@UpdTp.setter
	def UpdTp(self, value):
		self._UpdTp = value if value is not None else base_types.UninitialisedField(self, 'UpdTp', StatementUpdateTypeCodeAndDSSCode1Choice, False)

	@UpdTp.deleter
	def UpdTp(self):
		del self._UpdTp
		self._UpdTp = base_types.UninitialisedField(self, 'UpdTp', StatementUpdateTypeCodeAndDSSCode1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frqcy', type=Frequency25Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtceTp', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='QryRef', type=QueryReference2, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptDtTm', type=DateAndDateTime1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RptNb', type=Max5NumericText, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UpdTp', type=StatementUpdateTypeCodeAndDSSCode1Choice, min=0, max=1, mutex_group=None, array=False),
	))