# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InternalisationData1

class SettlementInternaliserClientType1(base_types._BaseFieldType):

	__slots__ = ["_Prfssnl", "_Rtl"]
	@property
	def Prfssnl(self):
		return self._Prfssnl

	@Prfssnl.setter
	def Prfssnl(self, value):
		self._Prfssnl = value if value is not None else base_types.UninitialisedField(self, 'Prfssnl', InternalisationData1, False)

	@Prfssnl.deleter
	def Prfssnl(self):
		del self._Prfssnl
		self._Prfssnl = base_types.UninitialisedField(self, 'Prfssnl', InternalisationData1, False)

	@property
	def Rtl(self):
		return self._Rtl

	@Rtl.setter
	def Rtl(self, value):
		self._Rtl = value if value is not None else base_types.UninitialisedField(self, 'Rtl', InternalisationData1, False)

	@Rtl.deleter
	def Rtl(self):
		del self._Rtl
		self._Rtl = base_types.UninitialisedField(self, 'Rtl', InternalisationData1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='Prfssnl', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Rtl', type=InternalisationData1, min=1, max=1, mutex_group=None, array=False),
	))