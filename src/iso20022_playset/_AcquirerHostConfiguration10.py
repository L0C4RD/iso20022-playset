# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from ._Max1025Text import Max1025Text
from ._Max35Text import Max35Text
from ._Max8Text import Max8Text
from ._MessageFunction47Code import MessageFunction47Code

class AcquirerHostConfiguration10(base_types._BaseFieldType):

	__slots__ = ["_HstId", "_MsgToSnd", "_PrtcolVrsn", "_XtrnlyTpSpprtd"]
	@property
	def HstId(self):
		return self._HstId

	@HstId.setter
	def HstId(self, value):
		self._HstId = value if type(value) != base_types.auto else self.make_default("HstId")

	@HstId.deleter
	def HstId(self):
		del self._HstId
		self._HstId = None

	@property
	def MsgToSnd(self):
		return self._MsgToSnd

	@MsgToSnd.setter
	def MsgToSnd(self, value):
		self._MsgToSnd = value if type(value) != base_types.auto else self.make_default("MsgToSnd")

	@MsgToSnd.deleter
	def MsgToSnd(self):
		del self._MsgToSnd
		self._MsgToSnd = None

	@property
	def PrtcolVrsn(self):
		return self._PrtcolVrsn

	@PrtcolVrsn.setter
	def PrtcolVrsn(self, value):
		self._PrtcolVrsn = value if type(value) != base_types.auto else self.make_default("PrtcolVrsn")

	@PrtcolVrsn.deleter
	def PrtcolVrsn(self):
		del self._PrtcolVrsn
		self._PrtcolVrsn = None

	@property
	def XtrnlyTpSpprtd(self):
		return self._XtrnlyTpSpprtd

	@XtrnlyTpSpprtd.setter
	def XtrnlyTpSpprtd(self, value):
		self._XtrnlyTpSpprtd = value if type(value) != base_types.auto else self.make_default("XtrnlyTpSpprtd")

	@XtrnlyTpSpprtd.deleter
	def XtrnlyTpSpprtd(self):
		del self._XtrnlyTpSpprtd
		self._XtrnlyTpSpprtd = None

	_field_defs = frozenset((
		base_types.FieldEntry(name='HstId', type=Max35Text, min=1, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='MsgToSnd', type=MessageFunction47Code, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='PrtcolVrsn', type=Max8Text, min=0, max=1, mutex_group=None, array=False),
		base_types.FieldEntry(name='XtrnlyTpSpprtd', type=Max1025Text, min=0, max=None, mutex_group=None, array=True),
	))