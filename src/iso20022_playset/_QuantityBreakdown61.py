# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._FinancialInstrumentQuantity33Choice import FinancialInstrumentQuantity33Choice
from ._GenericIdentification30 import GenericIdentification30
from ._GenericIdentification37 import GenericIdentification37

class QuantityBreakdown61(base_types._BaseFieldType):

	__slots__ = ["_LotNb", "_LotQty", "_SctiesSubBalTp"]
	@property
	def LotNb(self):
		return self._LotNb

	@LotNb.setter
	def LotNb(self, value):
		self._LotNb = value if type(value) != base_types.auto else self.make_default("LotNb")

	@LotNb.deleter
	def LotNb(self):
		del self._LotNb
		self._LotNb = None

	@property
	def LotQty(self):
		return self._LotQty

	@LotQty.setter
	def LotQty(self, value):
		self._LotQty = value if type(value) != base_types.auto else self.make_default("LotQty")

	@LotQty.deleter
	def LotQty(self):
		del self._LotQty
		self._LotQty = None

	@property
	def SctiesSubBalTp(self):
		return self._SctiesSubBalTp

	@SctiesSubBalTp.setter
	def SctiesSubBalTp(self, value):
		self._SctiesSubBalTp = value if type(value) != base_types.auto else self.make_default("SctiesSubBalTp")

	@SctiesSubBalTp.deleter
	def SctiesSubBalTp(self):
		del self._SctiesSubBalTp
		self._SctiesSubBalTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='LotNb', type=GenericIdentification37, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LotQty', type=FinancialInstrumentQuantity33Choice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesSubBalTp', type=GenericIdentification30, min=0, max=1, mutex_group=None, array=False),
	))