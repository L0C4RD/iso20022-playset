# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODate
from . import LockStatus1Code
from . import Max35Text

class PartyLockStatus1(base_types._BaseFieldType):

	__slots__ = ["_LckRsn", "_Sts", "_VldFr"]
	@property
	def LckRsn(self):
		return self._LckRsn

	@LckRsn.setter
	def LckRsn(self, value):
		self._LckRsn = value if value is not None else base_types.UninitialisedField(self, 'LckRsn', Max35Text, True)

	@LckRsn.deleter
	def LckRsn(self):
		del self._LckRsn
		self._LckRsn = base_types.UninitialisedField(self, 'LckRsn', Max35Text, True)

	@property
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', LockStatus1Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', LockStatus1Code, False)

	@property
	def VldFr(self):
		return self._VldFr

	@VldFr.setter
	def VldFr(self, value):
		self._VldFr = value if value is not None else base_types.UninitialisedField(self, 'VldFr', ISODate, False)

	@VldFr.deleter
	def VldFr(self):
		del self._VldFr
		self._VldFr = base_types.UninitialisedField(self, 'VldFr', ISODate, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='LckRsn', type=Max35Text, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='Sts', type=LockStatus1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='VldFr', type=ISODate, min=0, max=1, mutex_group=None, array=False),
	))