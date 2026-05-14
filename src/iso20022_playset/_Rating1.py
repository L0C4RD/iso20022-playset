# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._ISODateTime import ISODateTime
from ._Max35Text import Max35Text
from ._RatingValueIdentifier import RatingValueIdentifier

class Rating1(base_types._BaseFieldType):

	__slots__ = ["_RatgSchme", "_ValDt", "_ValId"]
	@property
	def RatgSchme(self):
		return self._RatgSchme

	@RatgSchme.setter
	def RatgSchme(self, value):
		self._RatgSchme = value if type(value) != base_types.auto else self.make_default("RatgSchme")

	@RatgSchme.deleter
	def RatgSchme(self):
		del self._RatgSchme
		self._RatgSchme = None

	@property
	def ValDt(self):
		return self._ValDt

	@ValDt.setter
	def ValDt(self, value):
		self._ValDt = value if type(value) != base_types.auto else self.make_default("ValDt")

	@ValDt.deleter
	def ValDt(self):
		del self._ValDt
		self._ValDt = None

	@property
	def ValId(self):
		return self._ValId

	@ValId.setter
	def ValId(self, value):
		self._ValId = value if type(value) != base_types.auto else self.make_default("ValId")

	@ValId.deleter
	def ValId(self):
		del self._ValId
		self._ValId = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='RatgSchme', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValDt', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='ValId', type=RatingValueIdentifier, min=1, max=1, mutex_group=None, array=False),
	))