# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import Max35Text

class PensionPolicy1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_Idr", "_SubIdr"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if value is not None else base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, False)

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = base_types.UninitialisedField(self, 'AddtlInf', AdditionalInformation15, False)

	@property
	def Idr(self):
		return self._Idr

	@Idr.setter
	def Idr(self, value):
		self._Idr = value if value is not None else base_types.UninitialisedField(self, 'Idr', Max35Text, False)

	@Idr.deleter
	def Idr(self):
		del self._Idr
		self._Idr = base_types.UninitialisedField(self, 'Idr', Max35Text, False)

	@property
	def SubIdr(self):
		return self._SubIdr

	@SubIdr.setter
	def SubIdr(self, value):
		self._SubIdr = value if value is not None else base_types.UninitialisedField(self, 'SubIdr', Max35Text, False)

	@SubIdr.deleter
	def SubIdr(self):
		del self._SubIdr
		self._SubIdr = base_types.UninitialisedField(self, 'SubIdr', Max35Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Idr', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='SubIdr', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
	))