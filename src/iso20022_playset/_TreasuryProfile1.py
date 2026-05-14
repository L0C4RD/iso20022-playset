# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODate import ISODate
from ._PartyRole5Choice import PartyRole5Choice
from ._PercentageRate import PercentageRate

class TreasuryProfile1(base_types._BaseFieldType):

	__slots__ = ["_Dt", "_Rate", "_TradrTp"]
	@property
	def Dt(self):
		return self._Dt

	@Dt.setter
	def Dt(self, value):
		self._Dt = value if type(value) != base_types.auto else self.make_default("Dt")

	@Dt.deleter
	def Dt(self):
		del self._Dt
		self._Dt = None

	@property
	def Rate(self):
		return self._Rate

	@Rate.setter
	def Rate(self, value):
		self._Rate = value if type(value) != base_types.auto else self.make_default("Rate")

	@Rate.deleter
	def Rate(self):
		del self._Rate
		self._Rate = None

	@property
	def TradrTp(self):
		return self._TradrTp

	@TradrTp.setter
	def TradrTp(self, value):
		self._TradrTp = value if type(value) != base_types.auto else self.make_default("TradrTp")

	@TradrTp.deleter
	def TradrTp(self):
		del self._TradrTp
		self._TradrTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Dt', type=ISODate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rate', type=PercentageRate, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TradrTp', type=PartyRole5Choice, min=1, max=1, mutex_group=None, array=False),
	))