# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyAndAmount
from . import BaseOneRate

class CapitalRequirement1(base_types._BaseFieldType):

	__slots__ = ["_BizRsk", "_CdtRsk", "_CntrPtyRsk", "_MktRsk", "_NtfctnBffr", "_OprlAndLglRsk", "_WndgDwnOrRstrgRsk"]
	@property
	def BizRsk(self):
		return self._BizRsk

	@BizRsk.setter
	def BizRsk(self, value):
		self._BizRsk = value if value is not None else base_types.UninitialisedField(self, 'BizRsk', ActiveCurrencyAndAmount, False)

	@BizRsk.deleter
	def BizRsk(self):
		del self._BizRsk
		self._BizRsk = base_types.UninitialisedField(self, 'BizRsk', ActiveCurrencyAndAmount, False)

	@property
	def CdtRsk(self):
		return self._CdtRsk

	@CdtRsk.setter
	def CdtRsk(self, value):
		self._CdtRsk = value if value is not None else base_types.UninitialisedField(self, 'CdtRsk', ActiveCurrencyAndAmount, False)

	@CdtRsk.deleter
	def CdtRsk(self):
		del self._CdtRsk
		self._CdtRsk = base_types.UninitialisedField(self, 'CdtRsk', ActiveCurrencyAndAmount, False)

	@property
	def CntrPtyRsk(self):
		return self._CntrPtyRsk

	@CntrPtyRsk.setter
	def CntrPtyRsk(self, value):
		self._CntrPtyRsk = value if value is not None else base_types.UninitialisedField(self, 'CntrPtyRsk', ActiveCurrencyAndAmount, False)

	@CntrPtyRsk.deleter
	def CntrPtyRsk(self):
		del self._CntrPtyRsk
		self._CntrPtyRsk = base_types.UninitialisedField(self, 'CntrPtyRsk', ActiveCurrencyAndAmount, False)

	@property
	def MktRsk(self):
		return self._MktRsk

	@MktRsk.setter
	def MktRsk(self, value):
		self._MktRsk = value if value is not None else base_types.UninitialisedField(self, 'MktRsk', ActiveCurrencyAndAmount, False)

	@MktRsk.deleter
	def MktRsk(self):
		del self._MktRsk
		self._MktRsk = base_types.UninitialisedField(self, 'MktRsk', ActiveCurrencyAndAmount, False)

	@property
	def NtfctnBffr(self):
		return self._NtfctnBffr

	@NtfctnBffr.setter
	def NtfctnBffr(self, value):
		self._NtfctnBffr = value if value is not None else base_types.UninitialisedField(self, 'NtfctnBffr', BaseOneRate, False)

	@NtfctnBffr.deleter
	def NtfctnBffr(self):
		del self._NtfctnBffr
		self._NtfctnBffr = base_types.UninitialisedField(self, 'NtfctnBffr', BaseOneRate, False)

	@property
	def OprlAndLglRsk(self):
		return self._OprlAndLglRsk

	@OprlAndLglRsk.setter
	def OprlAndLglRsk(self, value):
		self._OprlAndLglRsk = value if value is not None else base_types.UninitialisedField(self, 'OprlAndLglRsk', ActiveCurrencyAndAmount, False)

	@OprlAndLglRsk.deleter
	def OprlAndLglRsk(self):
		del self._OprlAndLglRsk
		self._OprlAndLglRsk = base_types.UninitialisedField(self, 'OprlAndLglRsk', ActiveCurrencyAndAmount, False)

	@property
	def WndgDwnOrRstrgRsk(self):
		return self._WndgDwnOrRstrgRsk

	@WndgDwnOrRstrgRsk.setter
	def WndgDwnOrRstrgRsk(self, value):
		self._WndgDwnOrRstrgRsk = value if value is not None else base_types.UninitialisedField(self, 'WndgDwnOrRstrgRsk', ActiveCurrencyAndAmount, False)

	@WndgDwnOrRstrgRsk.deleter
	def WndgDwnOrRstrgRsk(self):
		del self._WndgDwnOrRstrgRsk
		self._WndgDwnOrRstrgRsk = base_types.UninitialisedField(self, 'WndgDwnOrRstrgRsk', ActiveCurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizRsk', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtRsk', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CntrPtyRsk', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktRsk', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnBffr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprlAndLglRsk', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WndgDwnOrRstrgRsk', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))