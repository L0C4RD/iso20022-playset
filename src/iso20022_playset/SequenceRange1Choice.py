import base_types
import Max35Text
import SequenceRange1

class SequenceRange1Choice(base_types._BaseFieldType):

	__slots__ = ["_NEQSeq", "_EQSeq", "_FrToSeq", "_FrSeq", "_ToSeq"]
	@property
	def NEQSeq(self):
		return self._NEQSeq

	@NEQSeq.setter
	def NEQSeq(self, value):
		self._NEQSeq = value if type(value) != auto else self.make_default("NEQSeq")

	@NEQSeq.deleter
	def NEQSeq(self):
		del self._NEQSeq
		self._NEQSeq = None

	@property
	def EQSeq(self):
		return self._EQSeq

	@EQSeq.setter
	def EQSeq(self, value):
		self._EQSeq = value if type(value) != auto else self.make_default("EQSeq")

	@EQSeq.deleter
	def EQSeq(self):
		del self._EQSeq
		self._EQSeq = None

	@property
	def FrToSeq(self):
		return self._FrToSeq

	@FrToSeq.setter
	def FrToSeq(self, value):
		self._FrToSeq = value if type(value) != auto else self.make_default("FrToSeq")

	@FrToSeq.deleter
	def FrToSeq(self):
		del self._FrToSeq
		self._FrToSeq = None

	@property
	def FrSeq(self):
		return self._FrSeq

	@FrSeq.setter
	def FrSeq(self, value):
		self._FrSeq = value if type(value) != auto else self.make_default("FrSeq")

	@FrSeq.deleter
	def FrSeq(self):
		del self._FrSeq
		self._FrSeq = None

	@property
	def ToSeq(self):
		return self._ToSeq

	@ToSeq.setter
	def ToSeq(self, value):
		self._ToSeq = value if type(value) != auto else self.make_default("ToSeq")

	@ToSeq.deleter
	def ToSeq(self):
		del self._ToSeq
		self._ToSeq = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='NEQSeq', type=Max35Text, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='EQSeq', type=Max35Text, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='FrToSeq', type=SequenceRange1, min=1, max=None, mutex_group=1, array=True),
		base_types.FieldEntry(name='FrSeq', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='ToSeq', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

