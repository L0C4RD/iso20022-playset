# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max350Text
from . import SecuritiesAccount10
from . import SecurityIdentification7
from . import UnitOrFaceAmount1Choice

class SecuritiesProceeds1(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_PstngQty", "_RcncltnDtls", "_SctyId"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctDtls', SecuritiesAccount10, False)

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = base_types.UninitialisedField(self, 'AcctDtls', SecuritiesAccount10, False)

	@property
	def PstngQty(self):
		return self._PstngQty

	@PstngQty.setter
	def PstngQty(self, value):
		self._PstngQty = value if value is not None else base_types.UninitialisedField(self, 'PstngQty', UnitOrFaceAmount1Choice, False)

	@PstngQty.deleter
	def PstngQty(self):
		del self._PstngQty
		self._PstngQty = base_types.UninitialisedField(self, 'PstngQty', UnitOrFaceAmount1Choice, False)

	@property
	def RcncltnDtls(self):
		return self._RcncltnDtls

	@RcncltnDtls.setter
	def RcncltnDtls(self, value):
		self._RcncltnDtls = value if value is not None else base_types.UninitialisedField(self, 'RcncltnDtls', Max350Text, False)

	@RcncltnDtls.deleter
	def RcncltnDtls(self):
		del self._RcncltnDtls
		self._RcncltnDtls = base_types.UninitialisedField(self, 'RcncltnDtls', Max350Text, False)

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if value is not None else base_types.UninitialisedField(self, 'SctyId', SecurityIdentification7, False)

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = base_types.UninitialisedField(self, 'SctyId', SecurityIdentification7, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=SecuritiesAccount10, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='PstngQty', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='RcncltnDtls', type=Max350Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification7, min=1, max=1, mutex_group=None, array=False),
	))