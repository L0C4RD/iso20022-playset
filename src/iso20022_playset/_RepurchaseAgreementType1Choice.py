from . import base_types
from ._GeneralCollateral2 import GeneralCollateral2
from ._SpecificCollateral2 import SpecificCollateral2

class RepurchaseAgreementType1Choice(base_types._BaseFieldType):

	__slots__ = ["_SpcfcColl", "_GnlColl"]
	@property
	def SpcfcColl(self):
		return self._SpcfcColl

	@SpcfcColl.setter
	def SpcfcColl(self, value):
		self._SpcfcColl = value if type(value) != base_types.auto else self.make_default("SpcfcColl")

	@SpcfcColl.deleter
	def SpcfcColl(self):
		del self._SpcfcColl
		self._SpcfcColl = None

	@property
	def GnlColl(self):
		return self._GnlColl

	@GnlColl.setter
	def GnlColl(self, value):
		self._GnlColl = value if type(value) != base_types.auto else self.make_default("GnlColl")

	@GnlColl.deleter
	def GnlColl(self):
		del self._GnlColl
		self._GnlColl = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='SpcfcColl', type=SpecificCollateral2, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='GnlColl', type=GeneralCollateral2, min=0, max=1, mutex_group=1, array=False),
	))

