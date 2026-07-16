# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import Max1025Text
from . import Max35Text
from . import Max8Text
from . import MessageFunction47Code

class AcquirerHostConfiguration10(base_types._BaseFieldType):

	__slots__ = ["_HstId", "_MsgToSnd", "_PrtcolVrsn", "_XtrnlyTpSpprtd"]
	@property
	def HstId(self):
		return self._HstId

	@HstId.setter
	def HstId(self, value):
		self._HstId = value if value is not None else base_types.UninitialisedField(self, 'HstId', Max35Text, False)

	@HstId.deleter
	def HstId(self):
		del self._HstId
		self._HstId = base_types.UninitialisedField(self, 'HstId', Max35Text, False)

	@property
	def MsgToSnd(self):
		return self._MsgToSnd

	@MsgToSnd.setter
	def MsgToSnd(self, value):
		self._MsgToSnd = value if value is not None else base_types.UninitialisedField(self, 'MsgToSnd', MessageFunction47Code, True)

	@MsgToSnd.deleter
	def MsgToSnd(self):
		del self._MsgToSnd
		self._MsgToSnd = base_types.UninitialisedField(self, 'MsgToSnd', MessageFunction47Code, True)

	@property
	def PrtcolVrsn(self):
		return self._PrtcolVrsn

	@PrtcolVrsn.setter
	def PrtcolVrsn(self, value):
		self._PrtcolVrsn = value if value is not None else base_types.UninitialisedField(self, 'PrtcolVrsn', Max8Text, False)

	@PrtcolVrsn.deleter
	def PrtcolVrsn(self):
		del self._PrtcolVrsn
		self._PrtcolVrsn = base_types.UninitialisedField(self, 'PrtcolVrsn', Max8Text, False)

	@property
	def XtrnlyTpSpprtd(self):
		return self._XtrnlyTpSpprtd

	@XtrnlyTpSpprtd.setter
	def XtrnlyTpSpprtd(self, value):
		self._XtrnlyTpSpprtd = value if value is not None else base_types.UninitialisedField(self, 'XtrnlyTpSpprtd', Max1025Text, True)

	@XtrnlyTpSpprtd.deleter
	def XtrnlyTpSpprtd(self):
		del self._XtrnlyTpSpprtd
		self._XtrnlyTpSpprtd = base_types.UninitialisedField(self, 'XtrnlyTpSpprtd', Max1025Text, True)

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgToSnd', type=MessageFunction47Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtcolVrsn', type=Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtrnlyTpSpprtd', type=Max1025Text, min=0, max=None, mutex_group=None, array=True),
	))