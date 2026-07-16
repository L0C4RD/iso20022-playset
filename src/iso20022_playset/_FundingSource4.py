# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import FundingSourceType3Code
from . import Max35Text

class FundingSource4(base_types._BaseFieldType):

	__slots__ = ["_OthrTp", "_Ref", "_Tp"]
	@property
	def OthrTp(self):
		return self._OthrTp

	@OthrTp.setter
	def OthrTp(self, value):
		self._OthrTp = value if value is not None else base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@OthrTp.deleter
	def OthrTp(self):
		del self._OthrTp
		self._OthrTp = base_types.UninitialisedField(self, 'OthrTp', Max35Text, False)

	@property
	def Ref(self):
		return self._Ref

	@Ref.setter
	def Ref(self, value):
		self._Ref = value if value is not None else base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@Ref.deleter
	def Ref(self):
		del self._Ref
		self._Ref = base_types.UninitialisedField(self, 'Ref', Max35Text, False)

	@property
	def Tp(self):
		return self._Tp

	@Tp.setter
	def Tp(self, value):
		self._Tp = value if value is not None else base_types.UninitialisedField(self, 'Tp', FundingSourceType3Code, False)

	@Tp.deleter
	def Tp(self):
		del self._Tp
		self._Tp = base_types.UninitialisedField(self, 'Tp', FundingSourceType3Code, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='OthrTp', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Ref', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Tp', type=FundingSourceType3Code, min=0, max=1, mutex_group=None, array=False),
	))