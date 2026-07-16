# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AccountIdentification4Choice
from . import Max35Text

class AccountIdentificationSearchCriteria2Choice(base_types._BaseFieldType):

	__slots__ = ["_CTTxt", "_EQ", "_NCTTxt"]
	@property
	def CTTxt(self):
		return self._CTTxt

	@CTTxt.setter
	def CTTxt(self, value):
		self._CTTxt = value if value is not None else base_types.UninitialisedField(self, 'CTTxt', Max35Text, False)

	@CTTxt.deleter
	def CTTxt(self):
		del self._CTTxt
		self._CTTxt = base_types.UninitialisedField(self, 'CTTxt', Max35Text, False)

	@property
	def EQ(self):
		return self._EQ

	@EQ.setter
	def EQ(self, value):
		self._EQ = value if value is not None else base_types.UninitialisedField(self, 'EQ', AccountIdentification4Choice, False)

	@EQ.deleter
	def EQ(self):
		del self._EQ
		self._EQ = base_types.UninitialisedField(self, 'EQ', AccountIdentification4Choice, False)

	@property
	def NCTTxt(self):
		return self._NCTTxt

	@NCTTxt.setter
	def NCTTxt(self, value):
		self._NCTTxt = value if value is not None else base_types.UninitialisedField(self, 'NCTTxt', Max35Text, False)

	@NCTTxt.deleter
	def NCTTxt(self):
		del self._NCTTxt
		self._NCTTxt = base_types.UninitialisedField(self, 'NCTTxt', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='CTTxt', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='EQ', type=AccountIdentification4Choice, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='NCTTxt', type=Max35Text, min=0, max=1, mutex_group=1, array=False),
	))