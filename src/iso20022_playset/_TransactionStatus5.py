# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BaselineStatus3Code
from . import ISODateTime
from . import Max140Text

class TransactionStatus5(base_types._BaseFieldType):

	__slots__ = ["_ChngDtTm", "_Desc", "_Sts"]
	@property
	def ChngDtTm(self):
		return self._ChngDtTm

	@ChngDtTm.setter
	def ChngDtTm(self, value):
		self._ChngDtTm = value if value is not None else base_types.UninitialisedField(self, 'ChngDtTm', ISODateTime, False)

	@ChngDtTm.deleter
	def ChngDtTm(self):
		del self._ChngDtTm
		self._ChngDtTm = base_types.UninitialisedField(self, 'ChngDtTm', ISODateTime, False)

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
	def Sts(self):
		return self._Sts

	@Sts.setter
	def Sts(self, value):
		self._Sts = value if value is not None else base_types.UninitialisedField(self, 'Sts', BaselineStatus3Code, False)

	@Sts.deleter
	def Sts(self):
		del self._Sts
		self._Sts = base_types.UninitialisedField(self, 'Sts', BaselineStatus3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='ChngDtTm', type=ISODateTime, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Desc', type=Max140Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Sts', type=BaselineStatus3Code, min=1, max=1, mutex_group=None, array=False),
	))