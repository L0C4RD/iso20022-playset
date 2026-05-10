import base_types
import VoteTypeAndQuantity1
import Number
import YesNoIndicator

class IncentivePremiumType2Choice(base_types._BaseFieldType):

	__slots__ = ["_PerAttndee", "_PerScty", "_PerVote"]
	@property
	def PerAttndee(self):
		return self._PerAttndee

	@PerAttndee.setter
	def PerAttndee(self, value):
		self._PerAttndee = value if type(value) != auto else self.make_default("PerAttndee")

	@PerAttndee.deleter
	def PerAttndee(self):
		del self._PerAttndee
		self._PerAttndee = None

	@property
	def PerScty(self):
		return self._PerScty

	@PerScty.setter
	def PerScty(self, value):
		self._PerScty = value if type(value) != auto else self.make_default("PerScty")

	@PerScty.deleter
	def PerScty(self):
		del self._PerScty
		self._PerScty = None

	@property
	def PerVote(self):
		return self._PerVote

	@PerVote.setter
	def PerVote(self, value):
		self._PerVote = value if type(value) != auto else self.make_default("PerVote")

	@PerVote.deleter
	def PerVote(self):
		del self._PerVote
		self._PerVote = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='PerAttndee', type=YesNoIndicator, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PerScty', type=Number, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PerVote', type=VoteTypeAndQuantity1, min=1, max=None, mutex_group=1, array=True),
	))

