# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import DateQuarter1Choice

class Tax36(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_DtOrPrd"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, True)

	@property
	def DtOrPrd(self):
		return self._DtOrPrd

	@DtOrPrd.setter
	def DtOrPrd(self, value):
		self._DtOrPrd = value if value is not None else base_types.UninitialisedField(self, 'DtOrPrd', DateQuarter1Choice, False)

	@DtOrPrd.deleter
	def DtOrPrd(self):
		del self._DtOrPrd
		self._DtOrPrd = base_types.UninitialisedField(self, 'DtOrPrd', DateQuarter1Choice, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='DtOrPrd', type=DateQuarter1Choice, min=1, max=1, mutex_group=None, array=False),
	))