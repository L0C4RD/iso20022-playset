import base_types
import CurrencyAndAmount
import LineItemDetails12

class LineItem14(base_types._BaseFieldType):

	__slots__ = ["_OutsdngLineItmsTtlAmt", "_AccptdTtlNetAmt", "_OutsdngTtlNetAmt", "_OrdrdLineItmsTtlAmt", "_AccptdLineItmsTtlAmt", "_PdgLineItmsTtlAmt", "_PdgTtlNetAmt", "_LineItmDtls", "_OrdrdTtlNetAmt"]
	@property
	def OutsdngLineItmsTtlAmt(self):
		return self._OutsdngLineItmsTtlAmt

	@OutsdngLineItmsTtlAmt.setter
	def OutsdngLineItmsTtlAmt(self, value):
		self._OutsdngLineItmsTtlAmt = value if type(value) != auto else self.make_default("OutsdngLineItmsTtlAmt")

	@OutsdngLineItmsTtlAmt.deleter
	def OutsdngLineItmsTtlAmt(self):
		del self._OutsdngLineItmsTtlAmt
		self._OutsdngLineItmsTtlAmt = None

	@property
	def AccptdTtlNetAmt(self):
		return self._AccptdTtlNetAmt

	@AccptdTtlNetAmt.setter
	def AccptdTtlNetAmt(self, value):
		self._AccptdTtlNetAmt = value if type(value) != auto else self.make_default("AccptdTtlNetAmt")

	@AccptdTtlNetAmt.deleter
	def AccptdTtlNetAmt(self):
		del self._AccptdTtlNetAmt
		self._AccptdTtlNetAmt = None

	@property
	def OutsdngTtlNetAmt(self):
		return self._OutsdngTtlNetAmt

	@OutsdngTtlNetAmt.setter
	def OutsdngTtlNetAmt(self, value):
		self._OutsdngTtlNetAmt = value if type(value) != auto else self.make_default("OutsdngTtlNetAmt")

	@OutsdngTtlNetAmt.deleter
	def OutsdngTtlNetAmt(self):
		del self._OutsdngTtlNetAmt
		self._OutsdngTtlNetAmt = None

	@property
	def OrdrdLineItmsTtlAmt(self):
		return self._OrdrdLineItmsTtlAmt

	@OrdrdLineItmsTtlAmt.setter
	def OrdrdLineItmsTtlAmt(self, value):
		self._OrdrdLineItmsTtlAmt = value if type(value) != auto else self.make_default("OrdrdLineItmsTtlAmt")

	@OrdrdLineItmsTtlAmt.deleter
	def OrdrdLineItmsTtlAmt(self):
		del self._OrdrdLineItmsTtlAmt
		self._OrdrdLineItmsTtlAmt = None

	@property
	def AccptdLineItmsTtlAmt(self):
		return self._AccptdLineItmsTtlAmt

	@AccptdLineItmsTtlAmt.setter
	def AccptdLineItmsTtlAmt(self, value):
		self._AccptdLineItmsTtlAmt = value if type(value) != auto else self.make_default("AccptdLineItmsTtlAmt")

	@AccptdLineItmsTtlAmt.deleter
	def AccptdLineItmsTtlAmt(self):
		del self._AccptdLineItmsTtlAmt
		self._AccptdLineItmsTtlAmt = None

	@property
	def PdgLineItmsTtlAmt(self):
		return self._PdgLineItmsTtlAmt

	@PdgLineItmsTtlAmt.setter
	def PdgLineItmsTtlAmt(self, value):
		self._PdgLineItmsTtlAmt = value if type(value) != auto else self.make_default("PdgLineItmsTtlAmt")

	@PdgLineItmsTtlAmt.deleter
	def PdgLineItmsTtlAmt(self):
		del self._PdgLineItmsTtlAmt
		self._PdgLineItmsTtlAmt = None

	@property
	def PdgTtlNetAmt(self):
		return self._PdgTtlNetAmt

	@PdgTtlNetAmt.setter
	def PdgTtlNetAmt(self, value):
		self._PdgTtlNetAmt = value if type(value) != auto else self.make_default("PdgTtlNetAmt")

	@PdgTtlNetAmt.deleter
	def PdgTtlNetAmt(self):
		del self._PdgTtlNetAmt
		self._PdgTtlNetAmt = None

	@property
	def LineItmDtls(self):
		return self._LineItmDtls

	@LineItmDtls.setter
	def LineItmDtls(self, value):
		self._LineItmDtls = value if type(value) != auto else self.make_default("LineItmDtls")

	@LineItmDtls.deleter
	def LineItmDtls(self):
		del self._LineItmDtls
		self._LineItmDtls = None

	@property
	def OrdrdTtlNetAmt(self):
		return self._OrdrdTtlNetAmt

	@OrdrdTtlNetAmt.setter
	def OrdrdTtlNetAmt(self, value):
		self._OrdrdTtlNetAmt = value if type(value) != auto else self.make_default("OrdrdTtlNetAmt")

	@OrdrdTtlNetAmt.deleter
	def OrdrdTtlNetAmt(self):
		del self._OrdrdTtlNetAmt
		self._OrdrdTtlNetAmt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='OutsdngLineItmsTtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptdTtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngTtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrdLineItmsTtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptdLineItmsTtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgLineItmsTtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgTtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItmDtls', type=LineItemDetails12, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrdrdTtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))

