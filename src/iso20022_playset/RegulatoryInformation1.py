import base_types
import Max35Text

class RegulatoryInformation1(base_types._BaseFieldType):

	__slots__ = ["_Grp", "_Sctr", "_Brnch", "_Othr"]
	@property
	def Grp(self):
		return self._Grp

	@Grp.setter
	def Grp(self, value):
		self._Grp = value if type(value) != auto else self.make_default("Grp")

	@Grp.deleter
	def Grp(self):
		del self._Grp
		self._Grp = None

	@property
	def Sctr(self):
		return self._Sctr

	@Sctr.setter
	def Sctr(self, value):
		self._Sctr = value if type(value) != auto else self.make_default("Sctr")

	@Sctr.deleter
	def Sctr(self):
		del self._Sctr
		self._Sctr = None

	@property
	def Brnch(self):
		return self._Brnch

	@Brnch.setter
	def Brnch(self, value):
		self._Brnch = value if type(value) != auto else self.make_default("Brnch")

	@Brnch.deleter
	def Brnch(self):
		del self._Brnch
		self._Brnch = None

	@property
	def Othr(self):
		return self._Othr

	@Othr.setter
	def Othr(self, value):
		self._Othr = value if type(value) != auto else self.make_default("Othr")

	@Othr.deleter
	def Othr(self):
		del self._Othr
		self._Othr = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='Grp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sctr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Brnch', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Othr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))

