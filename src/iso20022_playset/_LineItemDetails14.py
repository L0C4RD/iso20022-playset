# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Adjustment6
from . import Charge25
from . import CountryCode
from . import CurrencyAndAmount
from . import Max70Text
from . import ProductCategory1Choice
from . import ProductCharacteristics1Choice
from . import ProductIdentifier2Choice
from . import Quantity9
from . import Tax22
from . import UnitPrice18

class LineItemDetails14(base_types._BaseFieldType):

	__slots__ = ["_Adjstmnt", "_FrghtChrgs", "_LineItmId", "_PdctChrtcs", "_PdctCtgy", "_PdctIdr", "_PdctNm", "_PdctOrgn", "_Qty", "_Tax", "_TtlAmt", "_UnitPric"]
	@property
	def Adjstmnt(self):
		return self._Adjstmnt

	@Adjstmnt.setter
	def Adjstmnt(self, value):
		self._Adjstmnt = value if value is not None else base_types.UninitialisedField(self, 'Adjstmnt', Adjustment6, True)

	@Adjstmnt.deleter
	def Adjstmnt(self):
		del self._Adjstmnt
		self._Adjstmnt = base_types.UninitialisedField(self, 'Adjstmnt', Adjustment6, True)

	@property
	def FrghtChrgs(self):
		return self._FrghtChrgs

	@FrghtChrgs.setter
	def FrghtChrgs(self, value):
		self._FrghtChrgs = value if value is not None else base_types.UninitialisedField(self, 'FrghtChrgs', Charge25, False)

	@FrghtChrgs.deleter
	def FrghtChrgs(self):
		del self._FrghtChrgs
		self._FrghtChrgs = base_types.UninitialisedField(self, 'FrghtChrgs', Charge25, False)

	@property
	def LineItmId(self):
		return self._LineItmId

	@LineItmId.setter
	def LineItmId(self, value):
		self._LineItmId = value if value is not None else base_types.UninitialisedField(self, 'LineItmId', Max70Text, False)

	@LineItmId.deleter
	def LineItmId(self):
		del self._LineItmId
		self._LineItmId = base_types.UninitialisedField(self, 'LineItmId', Max70Text, False)

	@property
	def PdctChrtcs(self):
		return self._PdctChrtcs

	@PdctChrtcs.setter
	def PdctChrtcs(self, value):
		self._PdctChrtcs = value if value is not None else base_types.UninitialisedField(self, 'PdctChrtcs', ProductCharacteristics1Choice, True)

	@PdctChrtcs.deleter
	def PdctChrtcs(self):
		del self._PdctChrtcs
		self._PdctChrtcs = base_types.UninitialisedField(self, 'PdctChrtcs', ProductCharacteristics1Choice, True)

	@property
	def PdctCtgy(self):
		return self._PdctCtgy

	@PdctCtgy.setter
	def PdctCtgy(self, value):
		self._PdctCtgy = value if value is not None else base_types.UninitialisedField(self, 'PdctCtgy', ProductCategory1Choice, True)

	@PdctCtgy.deleter
	def PdctCtgy(self):
		del self._PdctCtgy
		self._PdctCtgy = base_types.UninitialisedField(self, 'PdctCtgy', ProductCategory1Choice, True)

	@property
	def PdctIdr(self):
		return self._PdctIdr

	@PdctIdr.setter
	def PdctIdr(self, value):
		self._PdctIdr = value if value is not None else base_types.UninitialisedField(self, 'PdctIdr', ProductIdentifier2Choice, True)

	@PdctIdr.deleter
	def PdctIdr(self):
		del self._PdctIdr
		self._PdctIdr = base_types.UninitialisedField(self, 'PdctIdr', ProductIdentifier2Choice, True)

	@property
	def PdctNm(self):
		return self._PdctNm

	@PdctNm.setter
	def PdctNm(self, value):
		self._PdctNm = value if value is not None else base_types.UninitialisedField(self, 'PdctNm', Max70Text, False)

	@PdctNm.deleter
	def PdctNm(self):
		del self._PdctNm
		self._PdctNm = base_types.UninitialisedField(self, 'PdctNm', Max70Text, False)

	@property
	def PdctOrgn(self):
		return self._PdctOrgn

	@PdctOrgn.setter
	def PdctOrgn(self, value):
		self._PdctOrgn = value if value is not None else base_types.UninitialisedField(self, 'PdctOrgn', CountryCode, False)

	@PdctOrgn.deleter
	def PdctOrgn(self):
		del self._PdctOrgn
		self._PdctOrgn = base_types.UninitialisedField(self, 'PdctOrgn', CountryCode, False)

	@property
	def Qty(self):
		return self._Qty

	@Qty.setter
	def Qty(self, value):
		self._Qty = value if value is not None else base_types.UninitialisedField(self, 'Qty', Quantity9, False)

	@Qty.deleter
	def Qty(self):
		del self._Qty
		self._Qty = base_types.UninitialisedField(self, 'Qty', Quantity9, False)

	@property
	def Tax(self):
		return self._Tax

	@Tax.setter
	def Tax(self, value):
		self._Tax = value if value is not None else base_types.UninitialisedField(self, 'Tax', Tax22, True)

	@Tax.deleter
	def Tax(self):
		del self._Tax
		self._Tax = base_types.UninitialisedField(self, 'Tax', Tax22, True)

	@property
	def TtlAmt(self):
		return self._TtlAmt

	@TtlAmt.setter
	def TtlAmt(self, value):
		self._TtlAmt = value if value is not None else base_types.UninitialisedField(self, 'TtlAmt', CurrencyAndAmount, False)

	@TtlAmt.deleter
	def TtlAmt(self):
		del self._TtlAmt
		self._TtlAmt = base_types.UninitialisedField(self, 'TtlAmt', CurrencyAndAmount, False)

	@property
	def UnitPric(self):
		return self._UnitPric

	@UnitPric.setter
	def UnitPric(self, value):
		self._UnitPric = value if value is not None else base_types.UninitialisedField(self, 'UnitPric', UnitPrice18, False)

	@UnitPric.deleter
	def UnitPric(self):
		del self._UnitPric
		self._UnitPric = base_types.UninitialisedField(self, 'UnitPric', UnitPrice18, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Adjstmnt', type=Adjustment6, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='FrghtChrgs', type=Charge25, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LineItmId', type=Max70Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctChrtcs', type=ProductCharacteristics1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdctCtgy', type=ProductCategory1Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdctIdr', type=ProductIdentifier2Choice, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PdctNm', type=Max70Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PdctOrgn', type=CountryCode, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Qty', type=Quantity9, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tax', type=Tax22, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='TtlAmt', type=CurrencyAndAmount, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='UnitPric', type=UnitPrice18, min=0, max=1, mutex_group=None, array=False),
	))