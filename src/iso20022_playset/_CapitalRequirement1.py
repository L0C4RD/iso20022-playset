from . import base_types
from ._ActiveCurrencyAndAmount import ActiveCurrencyAndAmount
from ._BaseOneRate import BaseOneRate

class CapitalRequirement1(base_types._BaseFieldType):

	__slots__ = ["_CdtRsk", "_BizRsk", "_NtfctnBffr", "_OprlAndLglRsk", "_MktRsk", "_WndgDwnOrRstrgRsk", "_CntrPtyRsk"]
	@property
	def BizRsk(self):
		return self._BizRsk

	@BizRsk.setter
	def BizRsk(self, value):
		self._BizRsk = value if type(value) != base_types.auto else self.make_default("BizRsk")

	@BizRsk.deleter
	def BizRsk(self):
		del self._BizRsk
		self._BizRsk = None

	@property
	def CdtRsk(self):
		return self._CdtRsk

	@CdtRsk.setter
	def CdtRsk(self, value):
		self._CdtRsk = value if type(value) != base_types.auto else self.make_default("CdtRsk")

	@CdtRsk.deleter
	def CdtRsk(self):
		del self._CdtRsk
		self._CdtRsk = None

	@property
	def CntrPtyRsk(self):
		return self._CntrPtyRsk

	@CntrPtyRsk.setter
	def CntrPtyRsk(self, value):
		self._CntrPtyRsk = value if type(value) != base_types.auto else self.make_default("CntrPtyRsk")

	@CntrPtyRsk.deleter
	def CntrPtyRsk(self):
		del self._CntrPtyRsk
		self._CntrPtyRsk = None

	@property
	def MktRsk(self):
		return self._MktRsk

	@MktRsk.setter
	def MktRsk(self, value):
		self._MktRsk = value if type(value) != base_types.auto else self.make_default("MktRsk")

	@MktRsk.deleter
	def MktRsk(self):
		del self._MktRsk
		self._MktRsk = None

	@property
	def NtfctnBffr(self):
		return self._NtfctnBffr

	@NtfctnBffr.setter
	def NtfctnBffr(self, value):
		self._NtfctnBffr = value if type(value) != base_types.auto else self.make_default("NtfctnBffr")

	@NtfctnBffr.deleter
	def NtfctnBffr(self):
		del self._NtfctnBffr
		self._NtfctnBffr = None

	@property
	def OprlAndLglRsk(self):
		return self._OprlAndLglRsk

	@OprlAndLglRsk.setter
	def OprlAndLglRsk(self, value):
		self._OprlAndLglRsk = value if type(value) != base_types.auto else self.make_default("OprlAndLglRsk")

	@OprlAndLglRsk.deleter
	def OprlAndLglRsk(self):
		del self._OprlAndLglRsk
		self._OprlAndLglRsk = None

	@property
	def WndgDwnOrRstrgRsk(self):
		return self._WndgDwnOrRstrgRsk

	@WndgDwnOrRstrgRsk.setter
	def WndgDwnOrRstrgRsk(self, value):
		self._WndgDwnOrRstrgRsk = value if type(value) != base_types.auto else self.make_default("WndgDwnOrRstrgRsk")

	@WndgDwnOrRstrgRsk.deleter
	def WndgDwnOrRstrgRsk(self):
		del self._WndgDwnOrRstrgRsk
		self._WndgDwnOrRstrgRsk = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='BizRsk', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtRsk', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CntrPtyRsk', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MktRsk', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='NtfctnBffr', type=BaseOneRate, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OprlAndLglRsk', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='WndgDwnOrRstrgRsk', type=ActiveCurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

