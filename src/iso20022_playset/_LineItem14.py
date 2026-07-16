# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import CurrencyAndAmount
from . import LineItemDetails12

class LineItem14(base_types._BaseFieldType):

	__slots__ = ["_AccptdLineItmsTtlAmt", "_AccptdTtlNetAmt", "_LineItmDtls", "_OrdrdLineItmsTtlAmt", "_OrdrdTtlNetAmt", "_OutsdngLineItmsTtlAmt", "_OutsdngTtlNetAmt", "_PdgLineItmsTtlAmt", "_PdgTtlNetAmt"]
	@property
	def AccptdLineItmsTtlAmt(self):
		return self._AccptdLineItmsTtlAmt

	@AccptdLineItmsTtlAmt.setter
	def AccptdLineItmsTtlAmt(self, value):
		self._AccptdLineItmsTtlAmt = value if value is not None else base_types.UninitialisedField(self, 'AccptdLineItmsTtlAmt', CurrencyAndAmount, False)

	@AccptdLineItmsTtlAmt.deleter
	def AccptdLineItmsTtlAmt(self):
		del self._AccptdLineItmsTtlAmt
		self._AccptdLineItmsTtlAmt = base_types.UninitialisedField(self, 'AccptdLineItmsTtlAmt', CurrencyAndAmount, False)

	@property
	def AccptdTtlNetAmt(self):
		return self._AccptdTtlNetAmt

	@AccptdTtlNetAmt.setter
	def AccptdTtlNetAmt(self, value):
		self._AccptdTtlNetAmt = value if value is not None else base_types.UninitialisedField(self, 'AccptdTtlNetAmt', CurrencyAndAmount, False)

	@AccptdTtlNetAmt.deleter
	def AccptdTtlNetAmt(self):
		del self._AccptdTtlNetAmt
		self._AccptdTtlNetAmt = base_types.UninitialisedField(self, 'AccptdTtlNetAmt', CurrencyAndAmount, False)

	@property
	def LineItmDtls(self):
		return self._LineItmDtls

	@LineItmDtls.setter
	def LineItmDtls(self, value):
		self._LineItmDtls = value if value is not None else base_types.UninitialisedField(self, 'LineItmDtls', LineItemDetails12, True)

	@LineItmDtls.deleter
	def LineItmDtls(self):
		del self._LineItmDtls
		self._LineItmDtls = base_types.UninitialisedField(self, 'LineItmDtls', LineItemDetails12, True)

	@property
	def OrdrdLineItmsTtlAmt(self):
		return self._OrdrdLineItmsTtlAmt

	@OrdrdLineItmsTtlAmt.setter
	def OrdrdLineItmsTtlAmt(self, value):
		self._OrdrdLineItmsTtlAmt = value if value is not None else base_types.UninitialisedField(self, 'OrdrdLineItmsTtlAmt', CurrencyAndAmount, False)

	@OrdrdLineItmsTtlAmt.deleter
	def OrdrdLineItmsTtlAmt(self):
		del self._OrdrdLineItmsTtlAmt
		self._OrdrdLineItmsTtlAmt = base_types.UninitialisedField(self, 'OrdrdLineItmsTtlAmt', CurrencyAndAmount, False)

	@property
	def OrdrdTtlNetAmt(self):
		return self._OrdrdTtlNetAmt

	@OrdrdTtlNetAmt.setter
	def OrdrdTtlNetAmt(self, value):
		self._OrdrdTtlNetAmt = value if value is not None else base_types.UninitialisedField(self, 'OrdrdTtlNetAmt', CurrencyAndAmount, False)

	@OrdrdTtlNetAmt.deleter
	def OrdrdTtlNetAmt(self):
		del self._OrdrdTtlNetAmt
		self._OrdrdTtlNetAmt = base_types.UninitialisedField(self, 'OrdrdTtlNetAmt', CurrencyAndAmount, False)

	@property
	def OutsdngLineItmsTtlAmt(self):
		return self._OutsdngLineItmsTtlAmt

	@OutsdngLineItmsTtlAmt.setter
	def OutsdngLineItmsTtlAmt(self, value):
		self._OutsdngLineItmsTtlAmt = value if value is not None else base_types.UninitialisedField(self, 'OutsdngLineItmsTtlAmt', CurrencyAndAmount, False)

	@OutsdngLineItmsTtlAmt.deleter
	def OutsdngLineItmsTtlAmt(self):
		del self._OutsdngLineItmsTtlAmt
		self._OutsdngLineItmsTtlAmt = base_types.UninitialisedField(self, 'OutsdngLineItmsTtlAmt', CurrencyAndAmount, False)

	@property
	def OutsdngTtlNetAmt(self):
		return self._OutsdngTtlNetAmt

	@OutsdngTtlNetAmt.setter
	def OutsdngTtlNetAmt(self, value):
		self._OutsdngTtlNetAmt = value if value is not None else base_types.UninitialisedField(self, 'OutsdngTtlNetAmt', CurrencyAndAmount, False)

	@OutsdngTtlNetAmt.deleter
	def OutsdngTtlNetAmt(self):
		del self._OutsdngTtlNetAmt
		self._OutsdngTtlNetAmt = base_types.UninitialisedField(self, 'OutsdngTtlNetAmt', CurrencyAndAmount, False)

	@property
	def PdgLineItmsTtlAmt(self):
		return self._PdgLineItmsTtlAmt

	@PdgLineItmsTtlAmt.setter
	def PdgLineItmsTtlAmt(self, value):
		self._PdgLineItmsTtlAmt = value if value is not None else base_types.UninitialisedField(self, 'PdgLineItmsTtlAmt', CurrencyAndAmount, False)

	@PdgLineItmsTtlAmt.deleter
	def PdgLineItmsTtlAmt(self):
		del self._PdgLineItmsTtlAmt
		self._PdgLineItmsTtlAmt = base_types.UninitialisedField(self, 'PdgLineItmsTtlAmt', CurrencyAndAmount, False)

	@property
	def PdgTtlNetAmt(self):
		return self._PdgTtlNetAmt

	@PdgTtlNetAmt.setter
	def PdgTtlNetAmt(self, value):
		self._PdgTtlNetAmt = value if value is not None else base_types.UninitialisedField(self, 'PdgTtlNetAmt', CurrencyAndAmount, False)

	@PdgTtlNetAmt.deleter
	def PdgTtlNetAmt(self):
		del self._PdgTtlNetAmt
		self._PdgTtlNetAmt = base_types.UninitialisedField(self, 'PdgTtlNetAmt', CurrencyAndAmount, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AccptdLineItmsTtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='AccptdTtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItmDtls', type=LineItemDetails12, min=1, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='OrdrdLineItmsTtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OrdrdTtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngLineItmsTtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OutsdngTtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgLineItmsTtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdgTtlNetAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
	))