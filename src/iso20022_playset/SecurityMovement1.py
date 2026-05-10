from . import base_types
import SecuritiesAccount12
import Max35Text
import UnitOrFaceAmount1Choice
import SecurityIdentification7

class SecurityMovement1(base_types._BaseFieldType):

	__slots__ = ["_AcctDtls", "_SctiesQty", "_MvmntId", "_SctyId"]
	@property
	def AcctDtls(self):
		return self._AcctDtls

	@AcctDtls.setter
	def AcctDtls(self, value):
		self._AcctDtls = value if type(value) != auto else self.make_default("AcctDtls")

	@AcctDtls.deleter
	def AcctDtls(self):
		del self._AcctDtls
		self._AcctDtls = None

	@property
	def SctiesQty(self):
		return self._SctiesQty

	@SctiesQty.setter
	def SctiesQty(self, value):
		self._SctiesQty = value if type(value) != auto else self.make_default("SctiesQty")

	@SctiesQty.deleter
	def SctiesQty(self):
		del self._SctiesQty
		self._SctiesQty = None

	@property
	def MvmntId(self):
		return self._MvmntId

	@MvmntId.setter
	def MvmntId(self, value):
		self._MvmntId = value if type(value) != auto else self.make_default("MvmntId")

	@MvmntId.deleter
	def MvmntId(self):
		del self._MvmntId
		self._MvmntId = None

	@property
	def SctyId(self):
		return self._SctyId

	@SctyId.setter
	def SctyId(self, value):
		self._SctyId = value if type(value) != auto else self.make_default("SctyId")

	@SctyId.deleter
	def SctyId(self):
		del self._SctyId
		self._SctyId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AcctDtls', type=SecuritiesAccount12, min=1, max=2, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctiesQty', type=UnitOrFaceAmount1Choice, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MvmntId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SctyId', type=SecurityIdentification7, min=1, max=1, mutex_group=None, array=False),
	))

