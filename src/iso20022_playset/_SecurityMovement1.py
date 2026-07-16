# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text
from . import SecuritiesAccount12
from . import SecurityIdentification7
from . import UnitOrFaceAmount1Choice

class SecurityMovement1(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_MvmntId", "_SctiesQty", "_SctyId"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if value is not None else base_types.UninitialisedField(self, 'AcctDtls', SecuritiesAccount12, False)

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = base_types.UninitialisedField(self, 'AcctDtls', SecuritiesAccount12, False)

	@property
	def MvmntId(self):
		return self._MvmntId

	@MvmntId.setter
	def MvmntId(self, value):
		self._MvmntId = value if value is not None else base_types.UninitialisedField(self, 'MvmntId', Max35Text, False)

	@MvmntId.deleter
	def MvmntId(self):
		del self._MvmntId
		self._MvmntId = base_types.UninitialisedField(self, 'MvmntId', Max35Text, False)

	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if value is not None else base_types.UninitialisedField(self, 'SctiesQty', UnitOrFaceAmount1Choice, False)

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = base_types.UninitialisedField(self, 'SctiesQty', UnitOrFaceAmount1Choice, False)

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
		base_types.FieldEntry(name='AcctDtls', type=SecuritiesAccount12, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQty', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification7, min=1, max=1, mutex_group=None, array=False),
	))