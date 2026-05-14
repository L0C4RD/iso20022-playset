# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._AdditionalInformation15 import AdditionalInformation15
from ._Max350Text import Max350Text

class OtherTargetMarket1(base_types._BaseFieldType):

	__slots__ = ["_AddtlInf", "_TrgtMktTp"]
	@property
	def AddtlInf(self):
		return self._AddtlInf

	@AddtlInf.setter
	def AddtlInf(self, value):
		self._AddtlInf = value if type(value) != base_types.auto else self.make_default("AddtlInf")

	@AddtlInf.deleter
	def AddtlInf(self):
		del self._AddtlInf
		self._AddtlInf = None

	@property
	def TrgtMktTp(self):
		return self._TrgtMktTp

	@TrgtMktTp.setter
	def TrgtMktTp(self, value):
		self._TrgtMktTp = value if type(value) != base_types.auto else self.make_default("TrgtMktTp")

	@TrgtMktTp.deleter
	def TrgtMktTp(self):
		del self._TrgtMktTp
		self._TrgtMktTp = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='AddtlInf', type=AdditionalInformation15, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='TrgtMktTp', type=Max350Text, min=1, max=1, mutex_group=None, array=False),
	))