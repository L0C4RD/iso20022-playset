from . import base_types
from .IntraPositionMovementConfirmation002V09 import IntraPositionMovementConfirmation002V09

class SEMT_015_002_09():

	class Document(base_types._BaseFieldType):

		__slots__ = ["_IntraPosMvmntConf"]
		@property
		def IntraPosMvmntConf(self):
			return self._IntraPosMvmntConf

		@IntraPosMvmntConf.setter
		def IntraPosMvmntConf(self, value):
			self._IntraPosMvmntConf = value if type(value) != auto else self.make_default("IntraPosMvmntConf")

		@IntraPosMvmntConf.deleter
		def IntraPosMvmntConf(self):
			del self._IntraPosMvmntConf
			self._IntraPosMvmntConf = None

		_field_defs = frozenset((
			base_types.FieldEntry(name='IntraPosMvmntConf', type=IntraPositionMovementConfirmation002V09, min=1, max=1, mutex_group=None, array=False),
		))

