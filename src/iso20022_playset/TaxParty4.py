from . import base_types
from .TaxExemptionReasonFormat1Choice import TaxExemptionReasonFormat1Choice
from .Max35Text import Max35Text

class TaxParty4(base_types._BaseFieldType):

	__slots__ = ["_TaxId", "_TaxXmptnRsn", "_TaxTp", "_RegnId"]
	@property
	def TaxId(self):
		return self._TaxId

	@TaxId.setter
	def TaxId(self, value):
		self._TaxId = value if type(value) != auto else self.make_default("TaxId")

	@TaxId.deleter
	def TaxId(self):
		del self._TaxId
		self._TaxId = None

	@property
	def TaxXmptnRsn(self):
		return self._TaxXmptnRsn

	@TaxXmptnRsn.setter
	def TaxXmptnRsn(self, value):
		self._TaxXmptnRsn = value if type(value) != auto else self.make_default("TaxXmptnRsn")

	@TaxXmptnRsn.deleter
	def TaxXmptnRsn(self):
		del self._TaxXmptnRsn
		self._TaxXmptnRsn = None

	@property
	def TaxTp(self):
		return self._TaxTp

	@TaxTp.setter
	def TaxTp(self, value):
		self._TaxTp = value if type(value) != auto else self.make_default("TaxTp")

	@TaxTp.deleter
	def TaxTp(self):
		del self._TaxTp
		self._TaxTp = None

	@property
	def RegnId(self):
		return self._RegnId

	@RegnId.setter
	def RegnId(self, value):
		self._RegnId = value if type(value) != auto else self.make_default("RegnId")

	@RegnId.deleter
	def RegnId(self):
		del self._RegnId
		self._RegnId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TaxId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TaxXmptnRsn', type=TaxExemptionReasonFormat1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TaxTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RegnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

