# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import ISODateTime
from . import Max140Text
from . import Max4AlphaNumericText

class RequestHandling2(base_types._BaseFieldType):

	__slots__ = ["_Desc", "_StsCd", "_StsDtTm"]
	@property
	def Desc(self):
		return self._Desc

	@Desc.setter
	def Desc(self, value):
		self._Desc = value if value is not None else base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@Desc.deleter
	def Desc(self):
		del self._Desc
		self._Desc = base_types.UninitialisedField(self, 'Desc', Max140Text, False)

	@property
	def StsCd(self):
		return self._StsCd

	@StsCd.setter
	def StsCd(self, value):
		self._StsCd = value if value is not None else base_types.UninitialisedField(self, 'StsCd', Max4AlphaNumericText, False)

	@StsCd.deleter
	def StsCd(self):
		del self._StsCd
		self._StsCd = base_types.UninitialisedField(self, 'StsCd', Max4AlphaNumericText, False)

	@property
	def StsDtTm(self):
		return self._StsDtTm

	@StsDtTm.setter
	def StsDtTm(self, value):
		self._StsDtTm = value if value is not None else base_types.UninitialisedField(self, 'StsDtTm', ISODateTime, False)

	@StsDtTm.deleter
	def StsDtTm(self):
		del self._StsDtTm
		self._StsDtTm = base_types.UninitialisedField(self, 'StsDtTm', ISODateTime, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsCd', type=Max4AlphaNumericText, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='StsDtTm', type=ISODateTime, min=0, max=1, mutex_group=None, array=False),
	))