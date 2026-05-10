from . import base_types
import Max35Text
import AccountIdentification4Choice

class AccountIdentificationSearchCriteria2Choice(base_types._BaseFieldType):

	__slots__ = ["_EQ", "_NCTTxt", "_CTTxt"]
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
	def NCTTxt(self):
		return self._NCTTxt

	@NCTTxt.setter
	def NCTTxt(self, value):
		self._NCTTxt = value if type(value) != auto else self.make_default("NCTTxt")

	@NCTTxt.deleter
	def NCTTxt(self):
		del self._NCTTxt
		self._NCTTxt = None

	@property
	def CTTxt(self):
		return self._CTTxt

	@CTTxt.setter
	def CTTxt(self, value):
		self._CTTxt = value if type(value) != auto else self.make_default("CTTxt")

	@CTTxt.deleter
	def CTTxt(self):
		del self._CTTxt
		self._CTTxt = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='EQ', type=AccountIdentification4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NCTTxt', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='CTTxt', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))

