# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._PartyIdentificationAndAccount96 import PartyIdentificationAndAccount96
from ._PartyIdentificationAndAccount97 import PartyIdentificationAndAccount97

class CashParties24(base_types._BaseFieldType):

	__slots__ = ["_Cdtr", "_CdtrAgt", "_Intrmy", "_Intrmy2"]
	@property
	def Cdtr(self):
		return self._Cdtr

	@Cdtr.setter
	def Cdtr(self, value):
		self._Cdtr = value if type(value) != base_types.auto else self.make_default("Cdtr")

	@Cdtr.deleter
	def Cdtr(self):
		del self._Cdtr
		self._Cdtr = None

	@property
	def CdtrAgt(self):
		return self._CdtrAgt

	@CdtrAgt.setter
	def CdtrAgt(self, value):
		self._CdtrAgt = value if type(value) != base_types.auto else self.make_default("CdtrAgt")

	@CdtrAgt.deleter
	def CdtrAgt(self):
		del self._CdtrAgt
		self._CdtrAgt = None

	@property
	def Intrmy(self):
		return self._Intrmy

	@Intrmy.setter
	def Intrmy(self, value):
		self._Intrmy = value if type(value) != base_types.auto else self.make_default("Intrmy")

	@Intrmy.deleter
	def Intrmy(self):
		del self._Intrmy
		self._Intrmy = None

	@property
	def Intrmy2(self):
		return self._Intrmy2

	@Intrmy2.setter
	def Intrmy2(self, value):
		self._Intrmy2 = value if type(value) != base_types.auto else self.make_default("Intrmy2")

	@Intrmy2.deleter
	def Intrmy2(self):
		del self._Intrmy2
		self._Intrmy2 = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Cdtr', type=PartyIdentificationAndAccount96, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='CdtrAgt', type=PartyIdentificationAndAccount97, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrmy', type=PartyIdentificationAndAccount97, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Intrmy2', type=PartyIdentificationAndAccount97, min=0, max=1, mutex_group=None, array=False),
	))