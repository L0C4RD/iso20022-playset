# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max20KText
from . import Max35Text
from . import OutputFormat4Code

class DisputeDocumentation1(base_types._BaseFieldType):

	__slots__ = ["_Frmt", "_OthrFrmt", "_Tp", "_Val"]
	@property
	def Frmt(self):
		return self._Frmt

	@Frmt.setter
	def Frmt(self, value):
		self._Frmt = value if value is not None else base_types.UninitialisedField(self, 'Frmt', OutputFormat4Code, False)

	@Frmt.deleter
	def Frmt(self):
		del self._Frmt
		self._Frmt = base_types.UninitialisedField(self, 'Frmt', OutputFormat4Code, False)

	@property
	def OthrFrmt(self):
		return self._OthrFrmt

	@OthrFrmt.setter
	def OthrFrmt(self, value):
		self._OthrFrmt = value if value is not None else base_types.UninitialisedField(self, 'OthrFrmt', Max35Text, False)

	@OthrFrmt.deleter
	def OthrFrmt(self):
		del self._OthrFrmt
		self._OthrFrmt = base_types.UninitialisedField(self, 'OthrFrmt', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', Max35Text, False)

	@property
	def Val(self):
		return self._Val

	@Val.setter
	def Val(self, value):
		self._Val = value if value is not None else base_types.UninitialisedField(self, 'Val', Max20KText, False)

	@Val.deleter
	def Val(self):
		del self._Val
		self._Val = base_types.UninitialisedField(self, 'Val', Max20KText, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Frmt', type=OutputFormat4Code, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='OthrFrmt', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Val', type=Max20KText, min=1, max=1, mutex_group=None, array=False),
	))