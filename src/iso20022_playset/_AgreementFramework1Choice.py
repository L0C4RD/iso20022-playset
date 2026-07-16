# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import AgreementFramework1Code
from . import GenericIdentification30

class AgreementFramework1Choice(base_types._BaseFieldType):

	__slots__ = ["_AgrmtFrmwk", "_PrtryId"]
	@property
	def AgrmtFrmwk(self):
		return self._AgrmtFrmwk

	@AgrmtFrmwk.setter
	def AgrmtFrmwk(self, value):
		self._AgrmtFrmwk = value if value is not None else base_types.UninitialisedField(self, 'AgrmtFrmwk', AgreementFramework1Code, False)

	@AgrmtFrmwk.deleter
	def AgrmtFrmwk(self):
		del self._AgrmtFrmwk
		self._AgrmtFrmwk = base_types.UninitialisedField(self, 'AgrmtFrmwk', AgreementFramework1Code, False)

	@property
	def PrtryId(self):
		return self._PrtryId

	@PrtryId.setter
	def PrtryId(self, value):
		self._PrtryId = value if value is not None else base_types.UninitialisedField(self, 'PrtryId', GenericIdentification30, False)

	@PrtryId.deleter
	def PrtryId(self):
		del self._PrtryId
		self._PrtryId = base_types.UninitialisedField(self, 'PrtryId', GenericIdentification30, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='AgrmtFrmwk', type=AgreementFramework1Code, min=0, max=1, mutex_group=1, array=False),
		base_types.FieldEntry(name='PrtryId', type=GenericIdentification30, min=0, max=1, mutex_group=1, array=False),
	))