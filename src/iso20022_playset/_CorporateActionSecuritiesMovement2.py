# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._DateAndDateTimeChoice import DateAndDateTimeChoice
from ._Max35Text import Max35Text
from ._SecuritiesAccount9 import SecuritiesAccount9
from ._SecurityIdentification7 import SecurityIdentification7
from ._UnitOrFaceAmount1Choice import UnitOrFaceAmount1Choice

class CorporateActionSecuritiesMovement2(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_PstngDtTm", "_PstngId", "_PstngQty", "_SctyId"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != base_types.auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

	@property
	def PstngDtTm(self):
		return self._PstngDtTm

	@PstngDtTm.setter
	def PstngDtTm(self, value):
		self._PstngDtTm = value if type(value) != base_types.auto else self.make_default("PstngDtTm")

	@PstngDtTm.deleter
	def PstngDtTm(self):
		del self._PstngDtTm
		self._PstngDtTm = None

	@property
	def PstngId(self):
		return self._PstngId

	@PstngId.setter
	def PstngId(self, value):
		self._PstngId = value if type(value) != base_types.auto else self.make_default("PstngId")

	@PstngId.deleter
	def PstngId(self):
		del self._PstngId
		self._PstngId = None

	@property
	def PstngQty(self):
		return self._PstngQty

	@PstngQty.setter
	def PstngQty(self, value):
		self._PstngQty = value if type(value) != base_types.auto else self.make_default("PstngQty")

	@PstngQty.deleter
	def PstngQty(self):
		del self._PstngQty
		self._PstngQty = None

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != base_types.auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=SecuritiesAccount9, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngDtTm', type=DateAndDateTimeChoice, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngQty', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification7, min=1, max=1, mutex_group=None, array=False),
	))