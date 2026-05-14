# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODateTime import ISODateTime
from ._Max35Text import Max35Text
from ._TMSContactLevel1Code import TMSContactLevel1Code

class TMSTrigger1(base_types._BaseFieldType):

	__slots__ = ["_TMSCtctDtTm", "_TMSCtctLvl", "_TMSId"]
	@property
	def TMSCtctDtTm(self):
		return self._TMSCtctDtTm

	@TMSCtctDtTm.setter
	def TMSCtctDtTm(self, value):
		self._TMSCtctDtTm = value if type(value) != base_types.auto else self.make_default("TMSCtctDtTm")

	@TMSCtctDtTm.deleter
	def TMSCtctDtTm(self):
		del self._TMSCtctDtTm
		self._TMSCtctDtTm = None

	@property
	def TMSCtctLvl(self):
		return self._TMSCtctLvl

	@TMSCtctLvl.setter
	def TMSCtctLvl(self, value):
		self._TMSCtctLvl = value if type(value) != base_types.auto else self.make_default("TMSCtctLvl")

	@TMSCtctLvl.deleter
	def TMSCtctLvl(self):
		del self._TMSCtctLvl
		self._TMSCtctLvl = None

	@property
	def TMSId(self):
		return self._TMSId

	@TMSId.setter
	def TMSId(self, value):
		self._TMSId = value if type(value) != base_types.auto else self.make_default("TMSId")

	@TMSId.deleter
	def TMSId(self):
		del self._TMSId
		self._TMSId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='TMSCtctDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSCtctLvl', type=TMSContactLevel1Code, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TMSId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))