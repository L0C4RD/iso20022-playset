# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import Max3Number
from . import RestrictedFINXMax350Text

class SecuritiesTradeDetails103(base_types._BaseFieldType):

	__slots__ = ["_InstrPrcgAddtlDtls", "_NbOfDaysAcrd", "_OpngSttlmDt", "_TradDt"]
	@property
	def InstrPrcgAddtlDtls(self):
		return self._InstrPrcgAddtlDtls

	@InstrPrcgAddtlDtls.setter
	def InstrPrcgAddtlDtls(self, value):
		self._InstrPrcgAddtlDtls = value if value is not None else base_types.UninitialisedField(self, 'InstrPrcgAddtlDtls', RestrictedFINXMax350Text, False)

	@InstrPrcgAddtlDtls.deleter
	def InstrPrcgAddtlDtls(self):
		del self._InstrPrcgAddtlDtls
		self._InstrPrcgAddtlDtls = base_types.UninitialisedField(self, 'InstrPrcgAddtlDtls', RestrictedFINXMax350Text, False)

	@property
	def NbOfDaysAcrd(self):
		return self._NbOfDaysAcrd

	@NbOfDaysAcrd.setter
	def NbOfDaysAcrd(self, value):
		self._NbOfDaysAcrd = value if value is not None else base_types.UninitialisedField(self, 'NbOfDaysAcrd', Max3Number, False)

	@NbOfDaysAcrd.deleter
	def NbOfDaysAcrd(self):
		del self._NbOfDaysAcrd
		self._NbOfDaysAcrd = base_types.UninitialisedField(self, 'NbOfDaysAcrd', Max3Number, False)

	@property
	def OpngSttlmDt(self):
		return self._OpngSttlmDt

	@OpngSttlmDt.setter
	def OpngSttlmDt(self, value):
		self._OpngSttlmDt = value if value is not None else base_types.UninitialisedField(self, 'OpngSttlmDt', DateAndDateTime2Choice, False)

	@OpngSttlmDt.deleter
	def OpngSttlmDt(self):
		del self._OpngSttlmDt
		self._OpngSttlmDt = base_types.UninitialisedField(self, 'OpngSttlmDt', DateAndDateTime2Choice, False)

	@property
	def TradDt(self):
		return self._TradDt

	@TradDt.setter
	def TradDt(self, value):
		self._TradDt = value if value is not None else base_types.UninitialisedField(self, 'TradDt', DateAndDateTime2Choice, False)

	@TradDt.deleter
	def TradDt(self):
		del self._TradDt
		self._TradDt = base_types.UninitialisedField(self, 'TradDt', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InstrPrcgAddtlDtls', type=RestrictedFINXMax350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NbOfDaysAcrd', type=Max3Number, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OpngSttlmDt', type=DateAndDateTime2Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradDt', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=None, array=False),
	))