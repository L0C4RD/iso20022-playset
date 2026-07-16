# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max35Text
from . import TMSContactLevel1Code

class TMSTrigger1(base_types._BaseFieldType):

	__slots__ = ["_TMSCtctDtTm", "_TMSCtctLvl", "_TMSId"]
	@property
	def TMSCtctDtTm(self):
		return self._TMSCtctDtTm

	@TMSCtctDtTm.setter
	def TMSCtctDtTm(self, value):
		self._TMSCtctDtTm = value if value is not None else base_types.UninitialisedField(self, 'TMSCtctDtTm', ISODateTime, False)

	@TMSCtctDtTm.deleter
	def TMSCtctDtTm(self):
		del self._TMSCtctDtTm
		self._TMSCtctDtTm = base_types.UninitialisedField(self, 'TMSCtctDtTm', ISODateTime, False)

	@property
	def TMSCtctLvl(self):
		return self._TMSCtctLvl

	@TMSCtctLvl.setter
	def TMSCtctLvl(self, value):
		self._TMSCtctLvl = value if value is not None else base_types.UninitialisedField(self, 'TMSCtctLvl', TMSContactLevel1Code, False)

	@TMSCtctLvl.deleter
	def TMSCtctLvl(self):
		del self._TMSCtctLvl
		self._TMSCtctLvl = base_types.UninitialisedField(self, 'TMSCtctLvl', TMSContactLevel1Code, False)

	@property
	def TMSId(self):
		return self._TMSId

	@TMSId.setter
	def TMSId(self, value):
		self._TMSId = value if value is not None else base_types.UninitialisedField(self, 'TMSId', Max35Text, False)

	@TMSId.deleter
	def TMSId(self):
		del self._TMSId
		self._TMSId = base_types.UninitialisedField(self, 'TMSId', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='TMSCtctDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSCtctLvl', type=TMSContactLevel1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))