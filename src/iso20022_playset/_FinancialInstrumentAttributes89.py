# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ActiveCurrencyCode
from . import ContractSize1
from . import GenericIdentification165
from . import PhysicalTransferType4Code

class FinancialInstrumentAttributes89(base_types._BaseFieldType):

	__slots__ = ["_CtrctSz", "_DlvryTp", "_PricCcy", "_UndrlygId"]
	@property
	def CtrctSz(self):
		return self._CtrctSz

	@CtrctSz.setter
	def CtrctSz(self, value):
		self._CtrctSz = value if value is not None else base_types.UninitialisedField(self, 'CtrctSz', ContractSize1, False)

	@CtrctSz.deleter
	def CtrctSz(self):
		del self._CtrctSz
		self._CtrctSz = base_types.UninitialisedField(self, 'CtrctSz', ContractSize1, False)

	@property
	def DlvryTp(self):
		return self._DlvryTp

	@DlvryTp.setter
	def DlvryTp(self, value):
		self._DlvryTp = value if value is not None else base_types.UninitialisedField(self, 'DlvryTp', PhysicalTransferType4Code, False)

	@DlvryTp.deleter
	def DlvryTp(self):
		del self._DlvryTp
		self._DlvryTp = base_types.UninitialisedField(self, 'DlvryTp', PhysicalTransferType4Code, False)

	@property
	def PricCcy(self):
		return self._PricCcy

	@PricCcy.setter
	def PricCcy(self, value):
		self._PricCcy = value if value is not None else base_types.UninitialisedField(self, 'PricCcy', ActiveCurrencyCode, False)

	@PricCcy.deleter
	def PricCcy(self):
		del self._PricCcy
		self._PricCcy = base_types.UninitialisedField(self, 'PricCcy', ActiveCurrencyCode, False)

	@property
	def UndrlygId(self):
		return self._UndrlygId

	@UndrlygId.setter
	def UndrlygId(self, value):
		self._UndrlygId = value if value is not None else base_types.UninitialisedField(self, 'UndrlygId', GenericIdentification165, False)

	@UndrlygId.deleter
	def UndrlygId(self):
		del self._UndrlygId
		self._UndrlygId = base_types.UninitialisedField(self, 'UndrlygId', GenericIdentification165, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CtrctSz', type=ContractSize1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='DlvryTp', type=PhysicalTransferType4Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PricCcy', type=ActiveCurrencyCode, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UndrlygId', type=GenericIdentification165, min=1, max=1, mutex_group=None, array=False),
	))