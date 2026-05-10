import base_types
import Max35Text

class CharacterSearch1Choice(base_types._BaseFieldType):

	__slots__ = ["_NEQ", "_EQ", "_CT", "_NCT"]
	@property
	def NEQ(self):
		return self._NEQ

	@NEQ.setter
	def NEQ(self, value):
		self._NEQ = value if type(value) != auto else self.make_default("NEQ")

	@NEQ.deleter
	def NEQ(self):
		del self._NEQ
		self._NEQ = None

	@property
	def EQ(self):
		return self._EQ

	@EQ.setter
	def EQ(self, value):
		self._EQ = value if type(value) != auto else self.make_default("EQ")

	@EQ.deleter
	def EQ(self):
		del self._EQ
		self._EQ = None

	@property
	def CT(self):
		return self._CT

	@CT.setter
	def CT(self, value):
		self._CT = value if type(value) != auto else self.make_default("CT")

	@CT.deleter
	def CT(self):
		del self._CT
		self._CT = None

	@property
	def NCT(self):
		return self._NCT

	@NCT.setter
	def NCT(self, value):
		self._NCT = value if type(value) != auto else self.make_default("NCT")

	@NCT.deleter
	def NCT(self):
		del self._NCT
		self._NCT = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NEQ', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EQ', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CT', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NCT', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

