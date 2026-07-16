# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max35Text

class RegulatoryInformation1(base_types._BaseFieldType):

	__slots__ = ["_Brnch", "_Grp", "_Othr", "_Sctr"]
	@property
	def Brnch(self):
		return self._Brnch

	@Brnch.setter
	def Brnch(self, value):
		self._Brnch = value if value is not None else base_types.UninitialisedField(self, 'Brnch', Max35Text, False)

	@Brnch.deleter
	def Brnch(self):
		del self._Brnch
		self._Brnch = base_types.UninitialisedField(self, 'Brnch', Max35Text, False)

	@property
	def Grp(self):
		return self._Grp

	@Grp.setter
	def Grp(self, value):
		self._Grp = value if value is not None else base_types.UninitialisedField(self, 'Grp', Max35Text, False)

	@Grp.deleter
	def Grp(self):
		del self._Grp
		self._Grp = base_types.UninitialisedField(self, 'Grp', Max35Text, False)

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if value is not None else base_types.UninitialisedField(self, 'Othr', Max35Text, False)

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = base_types.UninitialisedField(self, 'Othr', Max35Text, False)

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if value is not None else base_types.UninitialisedField(self, 'Sctr', Max35Text, False)

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = base_types.UninitialisedField(self, 'Sctr', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Brnch', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Grp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))