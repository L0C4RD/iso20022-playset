# GPLv3.0 License.
# See LICENSE.md file in the project root for full license information.

from . import base_types
from . import BICIdentification1
from . import MessageIdentification1

class StatusReportRequestV03(base_types._BaseFieldType):

	__slots__ = ["_NttiesToBeRptd", "_ReqId"]
	@property
	def NttiesToBeRptd(self):
		return self._NttiesToBeRptd

	@NttiesToBeRptd.setter
	def NttiesToBeRptd(self, value):
		self._NttiesToBeRptd = value if value is not None else base_types.UninitialisedField(self, 'NttiesToBeRptd', BICIdentification1, True)

	@NttiesToBeRptd.deleter
	def NttiesToBeRptd(self):
		del self._NttiesToBeRptd
		self._NttiesToBeRptd = base_types.UninitialisedField(self, 'NttiesToBeRptd', BICIdentification1, True)

	@property
	def ReqId(self):
		return self._ReqId

	@ReqId.setter
	def ReqId(self, value):
		self._ReqId = value if value is not None else base_types.UninitialisedField(self, 'ReqId', MessageIdentification1, False)

	@ReqId.deleter
	def ReqId(self):
		del self._ReqId
		self._ReqId = base_types.UninitialisedField(self, 'ReqId', MessageIdentification1, False)

	_field_defs = frozenset((
		base_types.FieldEntry(name='NttiesToBeRptd', type=BICIdentification1, min=0, max=None, mutex_group=None, array=True),
		base_types.FieldEntry(name='ReqId', type=MessageIdentification1, min=1, max=1, mutex_group=None, array=False),
	))