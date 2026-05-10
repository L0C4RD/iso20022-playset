from . import base_types
from ._Max35Text import Max35Text
from ._LockStatus1Code import LockStatus1Code
from ._ISODate import ISODate

class PartyLockStatus1(base_types._BaseFieldType):

	__slots__ = ["_Sts", "_LckRsn", "_VldFr"]
	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if type(value) != base_types.auto else self.make_default("Sts")

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = None

	@property
	def LckRsn(self):
		return self._LckRsn

	@LckRsn.setter
	def LckRsn(self, value):
		self._LckRsn = value if type(value) != base_types.auto else self.make_default("LckRsn")

	@LckRsn.deleter
	def LckRsn(self):
		del self._LckRsn
		self._LckRsn = None

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if type(value) != base_types.auto else self.make_default("VldFr")

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Sts', type=LockStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='LckRsn', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='VldFr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))

