# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AdditionalInformation15
from . import Max350Text

class OtherTargetMarket1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_TrgtMktTp"]
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
	def TrgtMktTp(self):
		return self._TrgtMktTp

	@TrgtMktTp.setter
	def TrgtMktTp(self, value):
		self._TrgtMktTp = value if value is not None else base_types.UninitialisedField(self, 'TrgtMktTp', Max350Text, False)

	@TrgtMktTp.deleter
	def TrgtMktTp(self):
		del self._TrgtMktTp
		self._TrgtMktTp = base_types.UninitialisedField(self, 'TrgtMktTp', Max350Text, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtMktTp', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))