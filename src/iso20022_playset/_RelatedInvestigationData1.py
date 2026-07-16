# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import InvestigationLocationData1
from . import Max35Text

class RelatedInvestigationData1(base_types._BaseFieldType):

	__slots__ = ["_InvstgtnId", "_Lctn"]
	@property
	def InvstgtnId(self):
		return self._InvstgtnId

	@InvstgtnId.setter
	def InvstgtnId(self, value):
		self._InvstgtnId = value if value is not None else base_types.UninitialisedField(self, 'InvstgtnId', Max35Text, False)

	@InvstgtnId.deleter
	def InvstgtnId(self):
		del self._InvstgtnId
		self._InvstgtnId = base_types.UninitialisedField(self, 'InvstgtnId', Max35Text, False)

	@property
	def Lctn(self):
		return self._Lctn

	@Lctn.setter
	def Lctn(self, value):
		self._Lctn = value if value is not None else base_types.UninitialisedField(self, 'Lctn', InvestigationLocationData1, True)

	@Lctn.deleter
	def Lctn(self):
		del self._Lctn
		self._Lctn = base_types.UninitialisedField(self, 'Lctn', InvestigationLocationData1, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='InvstgtnId', type=Max35Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='Lctn', type=InvestigationLocationData1, min=0, max=None, mutex_group=None, array=True),
	))