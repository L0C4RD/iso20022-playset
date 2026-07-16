# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import DateAndDateTime2Choice
from . import DateType1Code

class DateFormat58Choice(base_types._BaseFieldType):

	__slots__ = ["_DtCd", "_DtOrDtTm"]
	@property
	def DtCd(self):
		return self._DtCd

	@DtCd.setter
	def DtCd(self, value):
		self._DtCd = value if value is not None else base_types.UninitialisedField(self, 'DtCd', DateType1Code, False)

	@DtCd.deleter
	def DtCd(self):
		del self._DtCd
		self._DtCd = base_types.UninitialisedField(self, 'DtCd', DateType1Code, False)

	@property
	def DtOrDtTm(self):
		return self._DtOrDtTm

	@DtOrDtTm.setter
	def DtOrDtTm(self, value):
		self._DtOrDtTm = value if value is not None else base_types.UninitialisedField(self, 'DtOrDtTm', DateAndDateTime2Choice, False)

	@DtOrDtTm.deleter
	def DtOrDtTm(self):
		del self._DtOrDtTm
		self._DtOrDtTm = base_types.UninitialisedField(self, 'DtOrDtTm', DateAndDateTime2Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='DtCd', type=DateType1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='DtOrDtTm', type=DateAndDateTime2Choice, min=0, max=1, mutex_group=1, array=False),
	))